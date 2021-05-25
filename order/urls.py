from django.urls import path

from order import views

urlpatterns = [
    # 3.1 订单提交接口
    path('ticket/submit/', views.TicketOrderSubmitView.as_view(), name="ticket_submit"),
    # 3.2 订单详情(支付、取消订单、删除订单)
    path('order/detail/<int:sn>/', views.OrderDetail.as_view(), name="order_detail"),
    # 3.3 我的订单列表
    path('order/list/', views.OrderListView.as_view(), name="order_list"),
]