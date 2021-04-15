from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# 这里弄一个单选的JobTypes，列表类型，里面每一个元素都是一个2元祖
JobTypes = [
    (0,"技术类"),
    (1,"产品类"),
    (2,"运营类"),
    (3,"设计类")
]

Cities = [
    (0,"北京"),
    (1,"上海"),
    (2,"深圳")
]

class Job(models.Model):# 这个Model是继承了django的Model，会有自动提示的，因为安装了Django库
    #定义职位类型,SmallIntegerField类型，这个字段是不允许为空的，所以blank=False，职位类型可以选择，定义一个choices，页面上展现的verbose_name名称
    job_type = models.SmallIntegerField(blank=False,choices=JobTypes,verbose_name="职位类别")
    #定义职位名称，字符类型的，可以设置最大长度，这个字段也是不能为空的，blank=False
    job_name = models.CharField(max_length=250,blank=False,verbose_name="职位名称")
    #职位的城市，用一个choices类似于枚举型来表示
    job_city = models.SmallIntegerField(choices=Cities,blank=False,verbose_name="工作地点")
    #职位职责和职位要求，文本类型就好。
    job_reponsibility = models.TextField(max_length=1024,verbose_name="职位职责")
    job_requirement = models.TextField(max_length=1024,blank=False,verbose_name="职位要求")

    #职位的创建人，最好是获取系统的登录用户，可以用models里面的外键引用，ForeignKey在Django里表示引用另外一个模型的对象，User是系统自带的对象，在上面要导入一下
    #因为是外键引用，当我们删除一个用户的时候，这个职位它里面的用户就无效了，所以涉及到删除时外键关联如何处理的逻辑，需要去指定on_delete的一个行为
    #on_delete有默认的（忽略），级联删除，把数据设置成null，我们这里把关联数据的值设成NULL，on_delete引用的是函数不用加(),创建人要允许为null，不然报错。
    creator = models.ForeignKey(User,verbose_name="创建人",on_delete=models.SET_NULL,null=True)
    created_date = models.DateTimeField(verbose_name="创建日期")
    modified_date = models.DateTimeField(verbose_name="修改时间")