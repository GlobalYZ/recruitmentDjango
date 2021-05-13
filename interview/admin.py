import csv

from django.contrib import admin
from django.http import HttpResponse
from django.db.models import Q
from interview.models import Candidate
from interview import candidate_field as cf
from datetime import datetime
from interview import dingtalk
import logging
import csv
# Register your models here.

logger = logging.getLogger(__name__)# 定义日志信息：用当前模块的运行的脚本的名字

exportable_fields = ('username','city','phone','bachelor_school','master_school','degree','first_result',
                     'first_interviewer_user','second_result','second_interviewer_user','hr_result','hr_score',
                     'hr_remark','hr_interviewer_user',)

# 通知一面面试官面试
def notify_interviewer(modeladmin, request, queryset):
    candidates = ""
    interviewers = ""
    for obj in queryset:
        candidates = obj.username + ";" + candidates
        interviewers = obj.first_interviewer_user.username + ";" + interviewers
    # 这里的消息发送到钉钉， 或者通过 Celery 异步发送到钉钉
    #send ("候选人 %s 进入面试环节，亲爱的面试官，请准备好面试： %s" % (candidates, interviewers) )
    # send_dingtalk_message.delay("候选人 %s 进入面试环节，亲爱的面试官，请准备好面试： %s" % (candidates, interviewers) )
    # messages.add_message(request, messages.INFO, '已经成功发送面试通知')


notify_interviewer.short_description = u'通知一面面试官'

# request是用户发起的请求，queryset是用户在界面上选择的结果列表里面的数据集合
def export_model_as_csv(modeladmin,request,queryset):
    response = HttpResponse(content_type='text/csv')
    field_list = exportable_fields
    response['Content-Disposition'] = 'attachment;filename=recruitment-candidates-list-%s.csv' %  (
        datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
    )
    # 写入表头
    writer = csv.writer(response)
    writer.writerow(
        # 参考 https://blog.csdn.net/weixin_44192923/article/details/88245398
        [queryset.model._meta.get_field(f).verbose_name.title() for f in field_list]
    )

    for obj in  queryset:
        # 单行的记录（每个字段的值），写入到csv文件
        csv_line_values = []
        for field in field_list:
            field_object = queryset.model._meta.get_field(field)
            field_value = field_object.value_from_object(obj)
            csv_line_values.append(field_value)
        writer.writerow(csv_line_values)

    # 谁在什么时候导出了多少条数据
    logger.info("%s exported %s candidate records" % (request.user,len(queryset)))

    return response

export_model_as_csv.short_description = "导出为CSV文件"
# 意思如果这个用户有export权限，那么allowed_permissions这个方法允许调用，允许了这个菜单才回展示出来，与下面的has_export_permission对应
export_model_as_csv.allowed_permissions = ('export',)

class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator','created_date','modified_date')

    actions = [export_model_as_csv,notify_interviewer,]

    # 当前用户是否有导出权限：
    def has_export_permission(self, request):
        opts = self.opts
        return request.user.has_perm('%s.%s' % (opts.app_label, "export"))

    list_display = (
        "username","city","bachelor_school","first_score","first_result","first_interviewer_user",
        "second_result","second_interviewer_user","hr_score","hr_result","last_editor"
    )

    # 筛选条件
    list_filter = ('city','first_result','second_result','hr_result','first_interviewer_user','second_interviewer_user','hr_interviewer_user',)
    # 查询功能
    search_fields = ('username','phone','email','bachelor_school')
    # 默认排序
    ordering = ('hr_result','second_result','first_result',)

    '''让只有HR才能在外简洁的修改面试官的方法，但是要和get_changelist_instance组合使用，它覆盖了父类的list_editable属性
    让这个属性的值，从get_list_editable的方法来获取'''
    def get_list_editable(self, request):
        group_names = self.get_group_names(request.user)

        if request.user.is_superuser or 'hr' in group_names:
            return ('first_interviewer_user','second_interviewer_user',)
        return ()

    def get_changelist_instance(self, request):
        """
        override admin method and list_editable property value
        with values returned by our custom method implementation.
        """
        self.list_editable = self.get_list_editable(request)
        return super(CandidateAdmin, self).get_changelist_instance(request)

    def get_group_names(self, user):# 把一个用户所有群组的名字都拿过来
        group_names = []
        for g in user.groups.all():
            group_names.append(g.name)
        return group_names

    '''只能让HR才能修改面试官'''
    def get_readonly_fields(self, request, obj):
        group_names = self.get_group_names(request.user)# 取到这个用户所属的群组角色
        if 'interviewer' in group_names:# 如果interviewer在它的角色列表里面，就返回下面那俩字段作为"只读字段"
            logger.info("interviewer is in user's group for %s" % request.user.username)
            return ('first_interviewer_user','second_interviewer_user',)
        return ()

    '''
    get_queryset在列表页展示的时候会默认调用，如果没有此方法会把当前所有数据直接返回；
    通过此方法，我们首先取得所有数据集，然后来判断当前用户的等级，如果是超级或管理员返回所有的数据集。
    如果不是，返回一个Candidate的一个子集，过滤条件是一面官=当前用户 或者 二面官=当前用户 ，这里用到了一个Q表达式。
    '''
    # 一面官和二面官就只能看到分到自己的简历
    def get_queryset(self, request):  # show data only owned by the user
        qs = super(CandidateAdmin, self).get_queryset(request)
        group_names = self.get_group_names(request.user)
        if request.user.is_superuser or 'hr' in group_names:
            return qs
        return Candidate.objects.filter(Q(first_interviewer_user=request.user) | Q(second_interviewer_user=request.user))


    # 一面面试官仅填写一面反馈， 二面面试官可以填写二面反馈
    def get_fieldsets(self, request, obj=None):
        group_names = self.get_group_names(request.user)# 登录的用户有哪些群组
        '''如果interviewer这个群组在登录的群组里面，并且与当前登录的用户一致，那么返回这个用户需要展示的字段'''
        if 'interviewer' in group_names and obj.first_interviewer_user == request.user:
            return cf.default_fieldsets_first
        if 'interviewer' in group_names and obj.second_interviewer_user == request.user:
            return cf.default_fieldsets_second
        return cf.default_fieldsets

    def save_model(self, request, obj, form, change):
        obj.last_editor = request.user.username
        if not obj.creator:
            obj.creator = request.user.username
        obj.modified_date = datetime.now()
        obj.save()

admin.site.register(Candidate,CandidateAdmin)
