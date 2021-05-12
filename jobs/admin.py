from django.contrib import admin
from jobs.models import Job
from datetime import datetime
# Register your models here.Django自带admin相关
# admin这里定义管理的属性，比如要把创建人默认的显示出来而不是选择
class JobAdmin(admin.ModelAdmin):# 继承自admin的ModelAdmin，它是一个管理类
    # list_display是ModelAdmin里面定义的特定含义的属性，这里我们可以定义在列表页展示哪些字段和不需要展示哪些字段，需要注册到下面
    list_display = ('job_name','job_type','job_city','creator','created_date','modified_date')
    # 在职位创建和修改里隐藏一些属性
    exclude = ('creator','created_date','modified_date')
    # 如果都隐藏了直接提交的话，那系统里是没有这些属性的，所以要利用ModelAdmin的父类定义的一个方法save_model，可以在保存模型之前做一些操作
    # 此函数与list_display、exclude类似，是定义好的属性，会被自动调用，
    def save_model(self, request, obj, form, change):
        obj.modified_date = datetime.now()
        obj.creator = request.user  # 这样可以把当前登录的用户设置成这个Model的创建人
        super().save_model(request,obj,form,change) # 需要调用一下父类的方法保存对象

# 将Job类注册到管理后台，页面上能显示
admin.site.register(Job,JobAdmin)
