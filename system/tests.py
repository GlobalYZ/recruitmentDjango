import json

from django.test import TestCase, Client

from system.models import Slider


class SliderTest(TestCase):
    """ 轮播图接口 """
    def setUp(self):
        Slider.objects.create(name='test1', types=11, img='a.jpg')
        Slider.objects.create(name='test2', types=12, img='b.jpg')
        # 请求对象
        self.client = Client()

    def test_slider_list(self):
        # 发起get请求
        response = self.client.get('/system/slider/list/')

        # 检查状态码
        self.assertEqual(response.status_code, 200)

    def test_slider_list_types(self):
        """ 按条件查询 """
        # 发起get请求
        response = self.client.get('/system/slider/list/', {
            'types': 11
        })

        # 检查状态码
        self.assertEqual(response.status_code, 200)
        data_list = json.loads(response.content)['objects']
        self.assertEqual(len(data_list), 1, '按条件查询失败')
