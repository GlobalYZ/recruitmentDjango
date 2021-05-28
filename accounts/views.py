import json

from django import http
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views.generic.base import View

from accounts.forms import LoginForm, RegisterForm
from utils.response import BadRequestJsonResponse, MethodNotAllowedJsonResponse, UnauthorizedJsonResponse, \
    ServerErrorJsonResponse
from accounts import serializers


def user_login(request):
    """ 用户登录 """
    if request.method == 'POST':
        # Form表单默认属性顺序(self, data=None, files=None, auto_id='id_%s', prefix=None,
        #                  initial=None, error_class=ErrorList, label_suffix=None,
        #                  empty_permitted=False, field_order=None, use_required_attribute=None, renderer=None):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            form.do_login(request)
            print('表单验证通过')
            return redirect('/accounts/user/info/')
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'user_login.html', {'form': form})

# 当打开用户信息时候发现没有将会自动跳转括号内路径，也可以在settings里设置LOGIN_URL = '/accounts/user/login/'
# @login_required(login_url='/accounts/user/login/')
@login_required
def user_info(request):
    """ 用户信息 """
    print(request.user)
    return render(request, 'user_info.html')


def user_logout(request):
    """ 用户退出登录 """
    logout(request)
    return redirect('/accounts/user/info/')


def user_api_login(request):
    """ 用户登录接口-POST """
    # 获取输入的内容
    if request.method == 'POST':
        # 表单验证
        form = LoginForm(request.POST)
        # 如果通过了验证，执行登录
        if form.is_valid():
            user = form.do_login(request)
            # 返回内容：用户的信息（用户的基本信息、详细信息）
            profile = user.profile# 1对1的反向查询，返回一个profile对象
            data = {
                'user': serializers.UserSerializer(user).to_dict(),
                'profile': serializers.UserProfileSerializer(profile).to_dict()
            }
            return http.JsonResponse(data)
            # return HttpResponse("oK")
        else:
            # 如果没有通过表单验证，返回表单的错误信息
            err = json.loads(form.errors.as_json())# form.errors.as_json()就是一个json，通过.loads转换成python对象
            return BadRequestJsonResponse(err)# 因为这个函数里要放入python对象,err里装的就是form里raise抛出的错误信息
    else:
        # 请求不被允许
        return MethodNotAllowedJsonResponse()


def user_api_logout(request):
    """ 用户退出接口 """
    logout(request)# from django.contrib.auth import logout
    return http.HttpResponse(status=201)# 给一个201的状态码说明已经退出了


class UserDetailView(View):
    """ 用户详细接口 ，这个地方不适用于@login_required，因为是前后端分离"""
    def get(self, request):# 登录完成之后，Django会把user设置到request这个模块里去
        # 获取用户信息
        user = request.user
        # 用户：是游客吗？
        if not user.is_authenticated:
            # 返回401状态码
            return UnauthorizedJsonResponse()
        else:
            # 返回详细信息
            profile = user.profile
            data = {
                'user': serializers.UserSerializer(user).to_dict(),
                'profile': serializers.UserProfileSerializer(profile).to_dict()
            }
            return http.JsonResponse(data)


def user_api_register(request):
    """ 用户注册 """
    # 1. 表单，验证用户输入的信息（用户名、昵称、验证码）
    # 2. 创建用户基础信息表、用户详细信息表
    # 3. 执行登录
    # 4. 保存登录日志
    pass


class UserRegisterView(FormView):
    """ 用户注册接口 """
    form_class = RegisterForm
    http_method_names = ['post']

    def form_valid(self, form):
        """ 表单已经通过验证 """
        result = form.do_register(request=self.request)
        if result is not None:
            user, profile = result
            data = {
                'user': serializers.UserSerializer(user).to_dict(),
                'profile': serializers.UserProfileSerializer(profile).to_dict()
            }
            return http.JsonResponse(data, status=201)
        return ServerErrorJsonResponse()

    def form_invalid(self, form):
        """ 表单没有通过验证 """
        err_list = json.loads(form.errors.as_json())
        return BadRequestJsonResponse(err_list)