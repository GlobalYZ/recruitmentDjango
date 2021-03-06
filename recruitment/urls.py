import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path,re_path,register_converter
from django.conf.urls import include,url
from django.utils.translation import gettext_lazy as _ # 用于下面的 'GlobalYZ后台管理系统'
from django.views.static import serve# 指向静态文件存放地址的规则
from app01 import views
from app01.urlconvert import MonConvert
# 注册自定义的url转换器
register_converter(MonConvert,"mm")

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r"^", include("jobs.urls")),# url和re_path用法是完全一致的
    path('grappelli/',include('grappelli.urls')),
    #registration这个APP提供了accounts目录下的不同应用，比如accounts的login、register、logout
    # path('accounts/', include('registration.backends.simple.urls')),
    # path('i18n/', include('django.conf.urls.i18n')),
    # path('testmiddle/',views.testMiddleware),# 测试中间件
    # 分发
    # re_path(r"^app01/",include(("app01.urls","app01"))),# 后面的app01就是命名空间的名称,组合成元组的形式，与视图函数里的反向解析相对应
    # 系统模块
    path('system/', include('system.urls')),
    # 用户账户模块
    path('accounts/', include('accounts.urls')),
    # 景点相关的URL
    path('sight/', include('sight.urls')),
    # 订单模块
    path('order/', include('order.urls')),
    # 富文本相关的配置
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # 统计报表
    path('master/', include('master.urls')),
]

# 出现错误的配置
handler500 = 'recruitment.views.page_500'

'''下面是Django框架提供的一个内置视图，可以按照它给定的规则进行配置，在开发的时候把项目当中的静态文件放到Django的内置服务器当中，
    使可直接进行访问，但不满足生产需要'''
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$',serve,{
            'document_root': settings.MEDIA_ROOT,
        }),
        path('__debug__/',include(debug_toolbar.urls)),
    ]


admin.site.site_header = _('GlobalYZ后台管理系统')