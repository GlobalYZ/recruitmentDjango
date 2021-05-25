import json

from django import http
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.db import connection

from system.forms import SendSmsCodeForm
from system.models import Slider
from utils.response import ServerErrorJsonResponse, BadRequestJsonResponse


def slider_list(request):
    """ 轮播图接口
    {
        "meta": {},
        "objects": []
    }
    """
    data = {
        'meta': {

        },
        'objects': []
    }
    queryset = Slider.objects.filter(is_valid=True)
    # 根据类型查询
    types = request.GET.get('types', None)
    if types:
        queryset = queryset.filter(types=types)
    for item in queryset:
        data['objects'].append({
            'id': item.id,
            'img_url': item.img.url,
            'target_url': item.target_url,
            'name': item.name
        })
    # return HttpResponse(data)
    return http.JsonResponse(data)


def cache_set(request):
    """ 写缓存 """
    cache.set('username', 'lisi')
    # 5之后自动删除
    cache.set('password', 'password', timeout=5)
    return HttpResponse('ok')


def cache_get(request):
    """ 读缓存 """
    value = cache.get('username')
    return HttpResponse(value)


def send_sms(request):
    pass
    # 1. 拿到手机号，判断是否为真实的手机号码

    # 2. 生成验证码，并存储
    # TODO 3. 调用短信的发送接口
    # 4. 告诉用户验证码发送是否成功（会把验证码直接告诉用户）


class SmsCodeView(FormView):
    form_class = SendSmsCodeForm

    def form_valid(self, form):
        """ 表单已经通过验证 """
        data = form.send_sms_code()
        if data is not None:
            return http.JsonResponse(data, status=201)
        return ServerErrorJsonResponse()

    def form_invalid(self, form):
        """ 表单没有通过验证 """
        err_list = json.loads(form.errors.as_json())
        return BadRequestJsonResponse(err_list)


def danger_sql(request):
    """ 危险的SQL注入
    正常输入：
    http://127.0.0.1:8000/system/danger/sql/?types=10
    异常输入：
    http://127.0.0.1:8000/system/danger/sql/?types=10' UNION select version(), database() -- ';
    """
    types = request.GET.get('types', '')
    # 1. 危险的写法
    # sql = "SELECT `name`, `img` FROM system_slider WHERE `types` ='{}';".format(types)
    # # sql = "SELECT `name`, `img` FROM system_slider WHERE `types` ='10' UNION select version(), database() -- ';';"
    # with connection.cursor() as c:
    #     c.execute(sql)
    #     data_list = c.fetchall()

    # 2. 安全的写法
    sql = "SELECT `name`, `img` FROM system_slider WHERE `types` =%s;"
    with connection.cursor() as c:
        c.execute(sql, (types, ))
        data_list = c.fetchall()
    return render(request, 'danger_sql.html', {
        'data_list': data_list
    })


def danger_xss(request):
    """ 跨站点脚本攻击
    输入测试：
    <script>window.alert('你好');window.location.href='http://www.imooc.com';</script>
    """
    if request.method == 'POST':
        name = request.POST.get('name', '')
        desc = request.POST.get('desc', '')
        Slider.objects.create(name=name, desc=desc, img='test.jpg')
        return redirect('.')
    else:
        types = 10
        sql = "SELECT `name`, `img`, `desc` FROM system_slider WHERE `types` =%s;"
        with connection.cursor() as c:
            c.execute(sql, (types, ))
            data_list = c.fetchall()
    return render(request, 'danger_xss.html', {
        'data_list': data_list
    })