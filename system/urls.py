from django.urls import path

from system import views

urlpatterns = [
    path('slider/list/', views.slider_list, name="slider_list"),
    path('cache/set/', views.cache_set, name="cache_set"),
    path('cache/get/', views.cache_get, name="cache_get"),
    # 发送验证码
    path('send/sms/', views.SmsCodeView.as_view(), name="send_sms"),
    # 危险的SQL注入
    path('danger/sql/', views.danger_sql, name="danger_sql"),
    # 跨站点脚本攻击
    path('danger/xss/', views.danger_xss, name="danger_xss"),
]