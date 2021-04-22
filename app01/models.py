from django.db import models

# Create your models here.
'''
web框架14day简单总结：
main.py:启动文件，封装了socket

1 urls.py:路径与视图函数映射关系 ---- url控制器
2 views.py:视图函数，固定有一个形式参数 environm，也有叫request的
3 templates文件夹:存放html文件 ---- 模板
4 models:在项目启动前，在数据库中创建表结构的 ---- 与数据库相关

'''

class Book(models.Model):# 括号里一定要有models.Model继承关系，所有的转化都是它给做的
    # 有以下字段
    id = models.AutoField(primary_key = True)# AutoField代表自增，primary_key参数限定约束，一个主键约束
    title = models.CharField(max_length = 32,unique=True)# CharField一个字符串，最大长度不能超过32,unique是说这个字段是唯一的
    # state = models.BooleanField()
    pub_date = models.DateField()# DateField存一个日期的
    # DecimalField是一个浮点型，类似于Double和Float，参数意思最多8位，要有两位是小数，也就是最大是它999999.99
    price = models.DecimalField(max_digits=8,decimal_places=2)
    publish = models.CharField(max_length=32)# CharField一个字符串，最大长度不能超过32

    def __str__(self):
        return self.title