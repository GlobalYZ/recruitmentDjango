from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import ProfileEditForm
from accounts.models import Profile, User


@admin.register(User)
class MyUserAdmin(UserAdmin):
    """ 用户基础信息管理 """
    # 列表中显示的内容
    list_display = ('username', 'nickname', 'is_active', 'is_staff', 'date_joined')
    # 搜索字段
    search_fields = ('username', 'nickname',)
    # 新增的表单
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('nickname', )}),
    )
    # 修改的表单
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('nickname', 'avatar')}),
    )
    actions = ['disable_user', 'enable_user']

    def disable_user(self, request, queryset):
        """ 批量禁用用户 """
        queryset.update(is_active=False)

    disable_user.short_description = '批量禁用用户'


    def enable_user(self, request, queryset):
        """ 批量启用用户 """
        queryset.update(is_active=True)

    enable_user.short_description = '批量启用用户'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ 用户详细信息表 """
    list_display = ('format_username', 'sex', 'age', 'created_at')
    # 每页显示5条数据
    list_per_page = 5
    # 关联的字段一次性查出，减少查询次数
    list_select_related = ('user', )
    # 快捷搜索
    list_filter = ('sex', )
    # 输入内容模糊匹配
    search_fields = ('username', 'user__nickname')
    # 表单中可以编辑的字段
    fields = ('real_name', 'email', 'phone_no', 'sex', 'age')
    # 自定义表单验证
    form = ProfileEditForm

    def format_username(self, obj):
        """ 用户名脱敏处理
        :param obj: Profile
        :return:
        """
        return obj.username[:3] + '***'
    # 修改列名称
    format_username.short_description = '用户名'