import json

from django import http
from django.db import transaction
from django.db.models import F, Q
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import FormView, ListView
from django.views.generic.detail import BaseDetailView

from order import serializers
from order.choices import OrderStatus
from order.forms import SubmitTicketOrderForm
from order.models import Order
from utils.response import BadRequestJsonResponse, NotFoundJsonResponse
from utils.views import login_required


def ticket_submit(request):
    """"""
    # 0. 验证用户是否已经登录
    # 1. 获取post数据
    # 2. 数据的验证（手机号、门票ID、库存）
    # 3. 关联用户、生成订单号、计算购买总价、生成订单（ORDER)
    # 4. 返回内容：订单ID
    pass


@method_decorator(login_required, name='dispatch')
class TicketOrderSubmitView(FormView):
    """ 3.1 门票订单提交接口 """
    form_class = SubmitTicketOrderForm
    http_method_names = ['post']

    def form_invalid(self, form):
        """ 表单未通过验证 """
        err = json.loads(form.errors.as_json())
        return BadRequestJsonResponse(err)

    def form_valid(self, form):
        obj = form.save(user=self.request.user)
        return http.JsonResponse({
            'sn': obj.sn
        }, status=201)


@method_decorator(login_required, name='dispatch')
class OrderDetail(BaseDetailView):
    slug_field = 'sn'
    slug_url_kwarg = 'sn'

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user, is_valid=True)

    def get(self, request, *args, **kwargs):
        """ GET: 订单详情 """
        order_obj = self.get_object()
        # 是否查询所有的信息
        data = serializers.OrderDetailSerializer(order_obj).to_dict()
        return http.JsonResponse(data)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        """ POST: 订单支付 """
        # 1. 选择支付方式：支付宝、微信
        # 2. 数据验证
        order_obj = self.get_object()
        if order_obj.status == OrderStatus.SUBMIT:
            # 3. 调用真实的支付（暂时省略）
            # 4. 改变订单状态
            order_obj.status = OrderStatus.PAID
            order_obj.save()
            order_obj.order_items.update(status=OrderStatus.PAID)
            return http.HttpResponse('', status=201)
        return http.HttpResponse('', status=200)

    def delete(self, request, *args, **kwargs):
        """ DELETE: 订单删除 """
        # 1. 获取订单对象
        order_obj = self.get_object()
        # 2. 验证数据（已支付、已取消）
        if order_obj.status == OrderStatus.CANCELED or order_obj.status == OrderStatus.PAID:
            # 3. 是否已经删除过了
            if order_obj.is_valid:
                order_obj.is_valid = False
                order_obj.save()
                return http.HttpResponse('', status=201)
            else:
                # 此处不用写，因为get_object已经触发了404
                pass
        return http.HttpResponse('', status=200)

    @transaction.atomic
    def put(self, request, *args, **kwargs):
        """ PUT： 取消订单 """
        # 1. 获取订单对象
        order_obj = self.get_object()
        # 2. 数据验证，状态判断
        if order_obj.status == OrderStatus.SUBMIT:
            # 3. 改变状态
            order_obj.status = OrderStatus.CANCELED
            order_obj.save()
            items = order_obj.order_items.filter(status=OrderStatus.SUBMIT)
            # 4. 加回已经扣减的库存
            for item in items:
                obj = item.content_object
                obj.remain_stock = F('remain_stock') + item.count
                obj.save()
            items.update(status=OrderStatus.CANCELED)
            return http.HttpResponse('', status=201)
        return http.HttpResponse('', status=200)


@method_decorator(login_required, name='dispatch')
class OrderListView(ListView):
    """ 3.3 我的订单列表 """
    paginate_by = 10  # 每页放10条数据

    def get_queryset(self):
        user = self.request.user
        query = Q(is_valid=True, user=user)
        # 按状态查询
        status = self.request.GET.get('status', None)
        if status and status != '0':
            query = query & Q(status=status)
        return Order.objects.filter(query)

    def render_to_response(self, context, **response_kwargs):
        """ 重写响应的返回，返回json """
        page_obj = context['page_obj']
        if page_obj is not None:
            data = serializers.OrderListSerializer(page_obj).to_dict()
            return http.JsonResponse(data)
        return NotFoundJsonResponse()

    def get_paginate_by(self, queryset):
        """ 根据接口参数limit来控制分页的大小 """
        page_size = self.request.GET.get('limit', None)
        return page_size or self.paginate_by
