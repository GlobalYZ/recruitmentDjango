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


class Book(models.Model):  # 括号里一定要有models.Model继承关系，所有的转化都是它给做的
    # 有以下字段
    id = models.AutoField(primary_key=True)  # AutoField代表自增，primary_key参数限定约束，一个主键约束
    title = models.CharField(max_length=32, unique=True)  # CharField一个字符串，最大长度不能超过32,unique是说这个字段是唯一的
    # state = models.BooleanField()
    pub_date = models.DateField()  # DateField存一个日期的
    # DecimalField是一个浮点型，类似于Double和Float，参数意思最多8位，要有两位是小数，也就是最大是它999999.99
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish = models.CharField(max_length=32)  # CharField一个字符串，最大长度不能超过32

    def __str__(self):
        return self.title


# ================================下面是关联表项目要用到的表结构===============================
# 一旦确定是一对多的关系：建立一对多的关系————————>在多的表中建立关联字段
# 一旦确定是多对多的关系：建立多对多的关系————————>创建第三张表（关联表）：id 和 两个关联字段
# 一旦确定是一对一的关系：建立一对一的关系————————>在两张表中的任意一张表建立关联字段+Unique

# Author和AuthorDetail是一对一
# Books表和Author是多对多
# Books表和Publish是多对一
# 作者详情表
class AuthorDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    birthday = models.DateField()
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)

    def __str__(self):
        return self.telephone

# 作者表
class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    # 设定与AuthorDetail表的一对一关系，注意如果不加to_fields，默认关联那张表的主键id
    authordetail = models.OneToOneField(to="AuthorDetail", on_delete=models.CASCADE)#  to_fields="nid",去掉了没报错。。。

    def __str__(self):
        return self.name

# 出版社表
class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self.name

#
class Books(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publishDate = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title

    # 下面这句一对多关联语句起到了mysql中两句话的作用：
    # 1.publish_id INT,
    # 2.FOREIGN KEY (publish_id) REFERENCES publish(id)
    # 这样它会在数据库中生成一个publish_id的字段
    publish = models.ForeignKey(to="Publish", on_delete=models.CASCADE)#  to_fields="nid",去掉了没报错。。。

    # 多对多，下面命令会直接生成第三张表，表名字叫books_authors，这张表的名字加这个字段
    authors = models.ManyToManyField(to="Author")#  to_fields="nid",去掉了没报错。。。

# 如果是多对多，需要创建第三张表，可以手写如下，但是Django通过语法可以一键生成，在上边
# class Book2Author(models.Model):
#     nid = models.AutoField(primary_key=True)
#     book = models.ForeignKey(to="Books")
#     author = models.ForeignKey(to="Author")# 不写to_fields默认关联其主键
