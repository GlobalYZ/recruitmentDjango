import json

from django.test import TestCase, Client

from accounts.models import User, Profile



class LoginTest(TestCase):

    def setUp(self):
        # 请求对象
        self.client = Client()
        user = User.objects.create_user(
            username='13800000001',
            password='A123123123',
            nickname='张三'
        )
        Profile.objects.create(user=user, username=user.username)

    def test_user_login_passed(self):
        """ 登录接口-登录成功 """
        # 发起post请求
        response = self.client.post('/accounts/user/api/login/', {
            'username': '13800000001',
            'password': 'A123123123'
        })

        # 检查状态码
        self.assertEqual(response.status_code, 200)

    def test_user_login_failure(self):
        """ 登录接口-登录失败 """
        # 发起post请求
        response = self.client.post('/accounts/user/api/login/', {
            'username': '13800000001',
            'password': 'A1231231231'
        })

        # 检查状态码
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn('密码不正确', str(data))



