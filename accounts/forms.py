import re
from django import forms
from django.contrib.auth import authenticate, login
from django.core.cache import cache
from django.utils.timezone import now
from django.db import transaction
from accounts.models import User, Profile
from utils import constants

'''
error_messages 覆盖字段引发异常后的错误显示
widget 定制界面显示方式（如：文本框、选择框）
disabled 禁用表单，界面上不可操作
redis相关操作：set、get、mset、mget、append、del、incr/decr(增加/减少1)
'''
class LoginForm(forms.Form):
    """ 登录表单 只需要用户名和密码"""
    username = forms.CharField(label='用户名', max_length=100, required=False, help_text='使用帮助', initial='admin')
    password = forms.CharField(label='密码', max_length=200, min_length=6, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 当前登录的用户
        self.user = None

    def clean_username(self):# 执行顺序① clean_定义好的字段 这是一个固定格式，
        """ 验证用户名 hook 钩子函数，Django表单会逐个调用clean_字段 开头的验证 """
        # cleaned_data--是已经触发了默认的字段属性验证之后，表单的实例数据字典里面是一个一个提交过来的数据
        username = self.cleaned_data['username']
        pattern = r'^1[0-9]{10}$'
        if not re.search(pattern, username):
            raise forms.ValidationError('手机号%s输入不正确', code='invalid_phone', params=(username, ))
        return username

    def clean(self):# 执行顺序② 属于重写
        """ 对用户名和密码进行统一验证 """
        data = super().clean()# 此clean()就是反回了self.cleaned_data的数据,它同时也会触发表单验证（上边的钩子函数）
        print("data:   ",data)# 里面是username和password的字典，如果用户名有问题则字典里只显示password的值
        # 如果单个字段有错误，直接返回，不执行后面的验证
        if self.errors:
            # print(self.errors.as_json()) 可以打印错误信息，转成json更直观
            return
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名或者是密码不正确')
        else:
            if not user.is_active:
                raise forms.ValidationError('该用户已经被禁用')
        self.user = user# 如果通过了上边的if和else，那么继续
        return data

    def do_login(self, request):
        """ 执行用户登录 """
        user = self.user
        # 调用登录
        login(request, user)# Django默认的方式是存储到session里了
        # 修改最后登录的时间，last_login是"用户模型"AbstractUser里继承的AbstractBaseUser的字段属性
        user.last_login = now()
        user.save()
        # TODO 保存登录历史
        return user


class RegisterForm(forms.Form):
    """ 用户注册 """
    username = forms.CharField(label='手机号码', max_length=16, required=True, error_messages={
        'required': '请输入手机号码'
    })
    password = forms.CharField(label='密码', max_length=128, required=True, error_messages={
        'required': '请输入密码'
    })
    nickname = forms.CharField(label='昵称', max_length=16, required=True, error_messages={
        'required': '请输入昵称'
    })
    sms_code = forms.CharField(label='验证码', max_length=6, required=True, error_messages={
        'required': '请输入验证码'
    })

    def clean_username(self):
        """ 验证用户名 hook 钩子函数 """
        username = self.cleaned_data['username']
        pattern = r'^1[0-9]{10}$'
        if not re.search(pattern, username):
            raise forms.ValidationError('手机号%s输入不正确',
                                        code='invalid_phone',
                                        params=(username, ))
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('手机号已经被使用')
        return username

    def clean_nickname(self):
        """ 昵称验证 """
        nickname = self.cleaned_data['nickname']
        if User.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError('昵称已经被使用')
        return nickname

    def clean(self):
        data = super().clean()
        if self.errors:
            return
        phone_num = self.cleaned_data.get('username', None)
        sms_code = self.cleaned_data.get('sms_code', None)

        # redis 中的验证码key
        key = '{}{}'.format(constants.REGISTER_MSM_CODE_KEY, phone_num)
        code = cache.get(key)
        # code 已失效
        if code is None:
            raise forms.ValidationError('验证码已经失效')
        if str(code) != sms_code:
            raise forms.ValidationError('验证码输入不正确')
        return data

    @transaction.atomic# 通过自动的事务控制来进行新创建
    def do_register(self, request):
        """ 执行注册 """
        data = self.cleaned_data
        version=request.headers.get('version', '')
        source=request.headers.get('source', '')
        try:
            # 1. 创建基础信息表
            user = User.objects.create_user(
                username=data.get('username', None),
                password=data.get('password', None),
                nickname=data.get('nickname', None)
            )
            # 2. 创建详细表
            profile = Profile.objects.create(
                user=user,
                username=user.username,
                version=version,
                source=source
            )
            # 3. 执行登录
            login(request, user)
            # 4. 记录登录日志
            user.last_login = now()
            user.save()
            ip = request.META.get('REMOTE_ADDR', '')
            user.add_login_record(username=user.username, ip=ip, source=source, version=version)
            return user, profile
        except Exception as e:
            print(e)
            return None

class ModifyForm(forms.Form):
    """ 用户修改信息 """
    username = forms.CharField(label='手机号码', max_length=16, required=True, error_messages={'required': '请输入手机号码'})
    real_name = forms.CharField(label='真实姓名', max_length=32, required=False, error_messages={'required': '姓名不可用'})
    avatar = forms.CharField(label='头像', max_length=32, required=False, error_messages={'required': '头像不可用'})
    email = forms.CharField(label='电子邮箱', max_length=128, required=False, error_messages={'required': 'Email不正确'})
    sex = forms.IntegerField(label='性别', required=False, error_messages={'required': '性别有误'})
    age = forms.IntegerField(label='年龄', required=False, error_messages={'required': '年龄有误'})

    def clean_age(self):
        """ 验证用户的年龄 """
        age = self.cleaned_data['age']
        if age is None:
            return User.objects.get(username=self.cleaned_data['username']).profile.age
        if int(age) >= 120 or int(age) <= 1:
            raise forms.ValidationError('年龄只能在1-120之间')
        return age
    def clean_sex(self):
        """ 验证用户的性别 """
        sex = self.cleaned_data['sex']
        if sex is None:
            return User.objects.get(username=self.cleaned_data['username']).profile.sex
        return sex
    def clean(self):
        data = super().clean()
        if self.errors:
            return
        return data
    @transaction.atomic
    def modify(self, request):
        """ 修改信息 """
        data = self.cleaned_data
        print('data         ',data)
        version=request.headers.get('version', '')
        source=request.headers.get('source', '')
        ip = request.META.get('REMOTE_ADDR', '')
        try:
            user = User.objects.get(username=data.get('username'))
            profile = user.profile
            user.avatar = data.get('avatar', user.avatar)
            user.email = data.get('email', user.email)
            profile.real_name = data.get('real_name', profile.real_name)
            profile.age = data.get('age', None)# 上边我已做过传默认值了，所以这个None不会生效
            profile.sex = data.get('sex', None)
            user.save()
            profile.save()
            user.add_login_record(username=user.username, ip=ip, source=source, version=version)
            return user, profile
        except Exception as e:
            print(e)
            return None




class ProfileEditForm(forms.ModelForm):
    """ 用户详细信息编辑 """

    class Meta:
        model = Profile
        fields = ('real_name', 'email', 'phone_no', 'sex', 'age')

    def clean_age(self):
        """ 验证用户的年龄 """
        age = self.cleaned_data['age']
        if int(age) >= 120 or int(age) <= 1:
            raise forms.ValidationError('年龄只能在1-120之间')
        return age

    def save(self, commit=False):# 重写，默认传递commit=True，意思是要不要直接插入到数据库，一般改为False
        obj = super().save(commit)
        # 此函数作用：保存数据时做一些其他的业务逻辑处理
        if not obj.source:
            obj.source = 'web'
            obj.save()
        return obj
