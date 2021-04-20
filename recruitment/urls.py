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
from django.urls import path,re_path
from django.conf.urls import include,url

from app01 import views

urlpatterns = [
    url(r"^",include("jobs.urls")),
    path('admin/', admin.site.urls),
    path('timer/',views.timer),# 当用户请求是127.0.0.1:8000/timer的时候，首先匹配到这个app01视图函数 如同views.timer(request)
    # 分发
    # re_path(r"app01/",include("app01.urls")),简写如下，以^开头直接去里面找对应的分发后面的app01是命名空间，组合成元组的形式
    re_path(r"^",include(("app01.urls","app01"))),

]

