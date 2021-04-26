"""recruitment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,register_converter
from django.conf.urls import include,url

from app01 import views
from app01.urlconvert import MonConvert

# 注册自定义的url转换器
register_converter(MonConvert,"mm")

urlpatterns = [
    url(r"^",include("jobs.urls")),# url和re_path用法是完全一致的
    path('admin/', admin.site.urls),
    path('timer/',views.timer),# 当用户请求是127.0.0.1:8000/timer的时候，首先匹配到这个app01视图函数 如同views.timer(request)
    path('index/',views.index),
    path('mysqlindex/',views.mysqlIndex),
    path('add/',views.add),# 数据库添加
    path('query/',views.query),# 数据库查询
    # 分发
    # re_path(r"app01/",include("app01.urls")),简写如下，以^开头直接去里面找对应的分发后面的app01是命名空间，组合成元组的形式
    re_path(r"^",include(("app01.urls","app01"))),# 后面的app01就是命名空间的名称，与视图函数里的反向解析相对应
    # path特征，可以创建一个有名分组，直接定义好数据类型
    path("articles/<int:year>",views.path_year),# 相当于path_year(request,2001)
    # 验证自定义的url转换器
    path("articles/<mm:month>",views.path_month),
]

