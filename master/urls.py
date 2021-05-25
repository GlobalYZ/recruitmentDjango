from django.urls import path

from master import views

urlpatterns = [
    # 统计报表
    path('', views.index, name='index'),
    # echarts的使用
    path('test/', views.test, name='test'),
]