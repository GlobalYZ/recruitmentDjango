from django.db import models
from django.utils.html import format_html
'''
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

ForeignKeyf(to,on_delete,**options) 外键关联，一对多
ManyToManyField(to,**options)  多对多  
OneToOneField(to,on_delete,parent_link=False,**options)  一对一
GenericForeignKey 复合关联

---on_delete 参数：
    |-PROTECT 受保护，不允许删除
    |-CASCADE 关联删除； 不让你删，除非你把关联的财产都删完了才可以删。
    |-SET_NULL 置空，设置为None，如有外键关联需要添加选项null=True
    |-SET_DEFAULT 可以设置被删了，默认给谁，需要添加选项default
    |-SET() 传参设置值
    |-DO_NOTHING 什么也不做，此为物理删除，如果有相关引用这个可能会报错，一般还是会选用逻辑删除
---related_name :是否需要反向引用，反向引用的名称就
---related_query_name :反向引用的名称
'''

class Book(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField代表自增，primary_key参数限定约束，一个主键约束
    title = models.CharField(max_length=32, unique=True)  # CharField一个字符串，最大长度不能超过32,unique是说这个字段是唯一的
    pub_date = models.DateField()  # DateField存一个日期的
    price = models.DecimalField(max_digits=8, decimal_places=2)# 参数意思最多8位，要有两位是小数，也就是最大是它999999.99
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
class AuthorDetail(models.Model):
    '''作者详情表'''
    nid = models.AutoField(primary_key=True)
    birthday = models.DateField()
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)
    def __str__(self):
        return self.telephone
class Author(models.Model):
    '''作者表'''
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    # 设定与AuthorDetail表的一对一关系，默认关联那张表的主键id，数据库中会生成一个authordetail_id
    authordetail = models.OneToOneField(to="AuthorDetail", on_delete=models.CASCADE,related_name="author")
    def __str__(self):
        return self.name
class Publish(models.Model):
    '''出版社表'''
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()
    def __str__(self):
        return self.name
class Books(models.Model):
    '''书籍表'''
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publishDate = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    read_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    # 这样它会在数据库中生成一个publish_id的字段
    publish = models.ForeignKey(to="Publish", on_delete=models.CASCADE)
    # 多对多，下面命令会直接生成第三张表，表名字叫books_authors，注意有个s，是本表名和下面字段名，里面有生成books_id和author_id
    authors = models.ManyToManyField(to="Author")
# -------------------------------------分割线--------------------------------------------------
# 员工表，在视图函数里的分组查询有用到
class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.CharField(max_length=32)
    province = models.CharField(max_length=32)
    def __str__(self):
        return self.name, self.salary

class CommonModel(models.Model):
    '''自定义模型的基类，如其它类也有此类属性字段，直接继承CommonModel即可'''
    created_at = models.DateTimeField('注册时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间', auto_now=True)
    class Meta:
        '''因为有此抽象属性，所以数据库中不会有这张表'''
        abstract = True
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
    class Meta:
        verbose_name = "文章"# 单用这一个会有复数+s的形式
        verbose_name_plural = "文章"
        db_table = 'Article'# 模型映射的数据库表的名称，可在此设置，建议每一张表都加上，不加的话数据库中生成的表名会与类不同
        # ordering = ['-pub_date']# 指定数据表的默认排序规则，按时间倒序
        # proxy = True# 如果这是一个代理类就添加此属性，上边需要继承某个类，如User，便可以新加函数等扩展功能
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
