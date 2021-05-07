from django.db import models

# Create your models here.
'''
web框架14day简单总结：
main.py:启动文件，封装了socket

1 urls.py:路径与视图函数映射关系 ---- url控制器
2 views.py:视图函数，固定有一个形式参数 environm，也有叫request的
3 templates文件夹:存放html文件 ---- 模板
4 models:在项目启动前，在数据库中创建表结构的 ---- 与数据库相关

AutoField 自增
BigAutoField 比较大的自增 64-bit integer
BigIntegerField 更大的整数 -9223372036854775808 to 9223372036854775807
BinaryField 只能存二进制
BooleanField 布尔值
CharField   字符串
DateField   存到天 2019-04-27
DateTimeField   存到秒 2019-04-27 17：53：21
DecimalField    存储小数位数的号码
DurationField   区间 有多少[DD] [HH:[MM:]]SS[.uuuuuu]
EmailField  Email，底层还是个字符串，能起到检测作用，数据库里没有这个
FileField   存储文件
FloatField 存储浮点
ImageField  存储图片，Django加了一层验证，本质上也是二进制
IntegerField    普通的整数
GenericIPAddressField   IP地址，支持IPV4和IPV6
NullBooleanField    允许为空的字段，和BooleanField相似，但能有NULL值
PositiveIntegerField    正整数 0 ~ 2147483647
PositiveSmallIntegerField   正的小数 0 ~ 32767
SlugField   也是个字符串，不怎么通用，新闻标签
SmallIntegerField   小整数
TextField   大的文本
URLField    是个URL
UUIDField   使用的 Python 的 UUID 库

ForeignKey 外键关联
ManyToManyField 多对多
OneToOneField 一对一

Django里一般需不要写ID，它会给默认加上，并且是自增的，设成了主键，自己写的话就用自己写的
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
    authordetail = models.OneToOneField(to="AuthorDetail", on_delete=models.CASCADE)  # to_fields="nid",去掉了没报错。。。

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
    read_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    # 下面这句一对多关联语句起到了mysql中两句话的作用：
    # 1.publish_id INT,
    # 2.FOREIGN KEY (publish_id) REFERENCES publish(id)
    # 这样它会在数据库中生成一个publish_id的字段
    publish = models.ForeignKey(to="Publish", on_delete=models.CASCADE)  # to_fields="nid",去掉了没报错。。。

    # 多对多，下面命令会直接生成第三张表，表名字叫books_authors，这张表的名字加这个字段
    authors = models.ManyToManyField(to="Author")  # to_fields="nid",去掉了没报错。。。


# 如果是多对多，需要创建第三张表，可以手写如下，但是Django通过语法可以一键生成，在上边
# class Book2Author(models.Model):
#     nid = models.AutoField(primary_key=True)
#     book = models.ForeignKey(to="Books")
#     author = models.ForeignKey(to="Author")# 不写to_fields默认关联其主键


# 员工表
class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.CharField(max_length=32)
    province = models.CharField(max_length=32)

    def __str__(self):
        return self.name, self.salary


from django.utils.html import format_html


class Account(models.Model):
    """账户表"""
    username = models.CharField(max_length=64, unique=True)  # unique 唯一的
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    register_date = models.DateTimeField(auto_now_add=True)  # 自动生成日期
    signature = models.CharField("签名", max_length=255, null=True)  # 可以加个中文解释 等同于+上一个 verbose_name = "签名"

    def __str__(self):
        return self.username


class Article(models.Model):
    """文章表"""
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    pub_date = models.DateTimeField()
    tags = models.ManyToManyField("Tag", blank=True)  # null=True可以不加，并且它对Mysql有效，但在Admin后台还是必填项，加blank就不必填了
    read_count = models.IntegerField(null=True)

    account = models.ForeignKey("Account", on_delete=models.CASCADE)

    # on_delete 参数：
    # CASCADE 关联删除； PROTECT 不让你删，除非你把关联的财产都删完了才可以删。
    # SET_NULL 置空，这里就是不知道谁是作者了
    # SET_DEFAULT 可以设置被删了，默认给谁

    class Meta:
        # verbose_name = "文章"# 用这个会有复数+s的形式
        verbose_name_plural = "文章"

    def get_comment(self):  # 返回评论
        return 10

    def get_tags(self):  # 返回这个文章关联的标签
        return ','.join([i.name for i in self.tags.all()])

    def __str__(self):
        return self.title


class Tag(models.Model):
    """标签表"""
    name = models.CharField(max_length=64, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    color_code = models.CharField(max_length=6)  # 颜色字段

    def colored_name(self):
        return format_html(
            '<span style="color: #{};">{}</span>',
            self.color_code,
            self.name,
        )

    def __str__(self):
        return self.name
