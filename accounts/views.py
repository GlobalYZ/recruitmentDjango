import json

from django import http
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
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
        form = LoginForm(data=request.POST)
        if form.is_valid():
            form.do_login(request)
            print('表单验证通过')
            return redirect('/accounts/user/info/')
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'user_login.html', {
        'form': form
    })


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
            # 返回内容：用户的信息（用户的基本信息、详细详细）
            profile = user.profile
            data = {
                'user': serializers.UserSerializer(user).to_dict(),
                'profile': serializers.UserProfileSerializer(profile).to_dict()
            }
            return http.JsonResponse(data)
        else:
            # 如果没有通过表单验证，返回表单的错误信息
            err = json.loads(form.errors.as_json())
            return BadRequestJsonResponse(err)
    else:
        # 请求不被允许
        return MethodNotAllowedJsonResponse()


def user_api_logout(request):
    """ 用户退出接口 """
    logout(request)
    return http.HttpResponse(status=201)


class UserDetailView(View):
    """ 用户详细接口 """

    def get(self, request):
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