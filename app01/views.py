# HttpResponse()是响应对象，（响应首行，消息头，响应体），Django已经帮做好首行和消息头，这里只需加入字符串的响应体
#
from django.shortcuts import render,HttpResponse

# Create your views here.
# 视图函数这里必须要传request，它是通过urls文件里的path传过来的
from django.urls import reverse


def timer(request):
    import time
    print(request.method)# GET POST
    print(request.GET,request.POST)# QueryDict的字典对象，可以根据request.GET.get("name")取值
    print(request.path)# url:协议：//IP：port/路径？请求数据，，，打印的是端口号之后，？之前的路径
    print(request.get_full_path)# 区别于上边，全打印出来

    ctime = time.time()
    # render()方法给封装好了，填入timer。html会自动去templates文件夹下去找
    # 把数据嵌入到html中，只需在第三个参数上传递即可，相当于把变量传递了，html那边的名字是和data保持一致的
    return render(request,"timer.html",{"date":ctime})# render方法会会渲染模板文件（html）成一个html文件，templates里都是模板文件

def special_case_2003(request):
    # 反向解析，给一个别名，通过reverse可解析出地址，在任意函数中都可以调用,加上命名空间更精准
    url = reverse("app01:s_c_2003")
    print("url命名空间:    -------      ",url)
    # 如果解析地址中含正则表达式，则需要传入一个符合该正则表达式的任意值代理匹配才可以
    url = reverse("app01:y_a",args=(7788,))# r"^articles/([0-9]{4})/$"
    print("url:    -------      ",url)

    return HttpResponse("special_case_2003")

def year_archive(request,year):
    return HttpResponse(year)

def month_archive(request,y,m):
    return HttpResponse(y + "  " + m)

def article_detail(requet,year,month,detail):
    return HttpResponse(year + " - " + month + " - " + detail)

def path_year(request,year):
    print(type(year))# 输出类型是<class 'int'>，得益于主urls里的有名分组，否则将是字符串类型
    return HttpResponse("path_year```")
def path_month(request,month):
    print(type(month))
    return HttpResponse("path_month```")

def index(request):
    '''
    模板语法：两种情况
    ① 变量    {{  }}
       1. 涉及到深度查询,用句点符
       2. 涉及到数据转换，用过滤器      {{val|filter_name:参数}}
    ② 标签    {%  %}


    :param request:
    :return:
    '''
    name = 'hahaha'
    i = 10
    l = [111,222,333]
    info = {'name':'hahha','age':'22'}
    b = True
    class Person(object):
        def __init__(self,name,age):
            self.name = name
            self.age = age
    alex = Person("alex",22)
    egon = Person('egon',33)
    personList = [alex,egon]

    # ---------------------过滤器------------------------
    import datetime
    now = datetime.datetime.now()
    person_List = []
    file_size = 1231423423
    text = "hello python hi luffycity go java linux"

    user = "洋哥"
    # user = None

    return render(request,"timer.html",locals())# 由于变量名多，一一写入麻烦，可以用locals()方法将其一起传入，但名字要对应一致

# 需要先导入
from app01.models import Book

def mysqlIndex(request):
    # ==================================添加表记录========================================
    # 方式一
    # book_obj = Book(id=1,title="python红宝书",price=100,pub_date="2020-12-12",publish="洋哥出版社")
    # book_obj.save()

    # 方式二 creat返回值就是当前生成的这条对象记录
    # id因为已设置成自增，故可以不传，此方式会直接执行后边的创建，返回给book_obj，无需save，
    # book_obj = Book.objects.create(title="php",price=100,pub_date="2020-12-18",publish="洋哥出版社")
    # print(book_obj.title)
    # print(book_obj.price)
    # print(book_obj.pub_date)

    # ==================================查询表记录API========================================
    '''
    1 方法的返回值
    2 方法的调用者

    '''
    # 1、all()方法，返回值是一个queryset对象
    book_list = Book.objects.all()
    # 打印出来的是Django里特有的QuerySet类型对象，类似于列表中的存放了一个一个对象[obj1,obj2,obj3···]
    print(book_list)# 在models里的Book类里要写好__srt__方法，打印出实际想要的效果
    for obj in book_list:
        print(obj.title,obj.price)

    print(book_list[1].title)

    # 2、first()、last()：调用者：QuerySet对象，返回值：model对象
    book = Book.objects.all().first()
    book = Book.objects.all()[0]# 与上者等同

    # 3、filter() 返回值：QuerySet对象，所以同样可以.first()
    book_list = Book.objects.filter(price=100)# [obj1,obj2,···]
    print(book_list)
    book_obj = Book.objects.filter(price=100).first()
    book_objects = Book.objects.filter(price=100,publish="洋哥出版社")
    print("-----------------",book_objects)

    # 4、get() 有且只有一个查询结果时才有意义，返回model对象，如有多个符合条件或没有符合条件，则报错
    book_obj = Book.objects.get(title="go")
    # book_obj = Book.objects.get(price=100) 报错
    print(book_obj.price)

    # 5、exclude()排除某项，返回值QuerySet
    ret = Book.objects.exclude(title="go")
    print(ret)

    # 6、order_by()排序，可多选，调用者：QuerySet，返回值：也是QuerySet
    ret = Book.objects.all().order_by("-id")# 默认按ASC有小到大排序，加上-号，则成为DESC由大到小排序
    ret = Book.objects.all().order_by("price","id")# 优先以price排，如相等，按id排
    print(ret)

    # 7、count() 调用者：QuerySet，返回值：int
    ret = Book.objects.all().count()
    print(ret)

    # 8、exist() 这样实际调用会使用LIMIT 1，随意查看一条语句，只要有存在则返回True，比直接all()要快很多，all()相当于select *
    ret = Book.objects.all().exists()
    if ret:
        print("OK")

    # 9、values()方法，可以直接循环取每一个对象的特有字段，返回的是一个含有字典的列表，调用者：QuerySet，返回值：QuerySet
    '''
    相当于是这样的操作原理
    temp = []
    for obj in Book.objects.all()
        temp.append({
            "price" = obj.price
        })
    return temp
    '''
    # ret = Book.objects.values("price") 这样也可以，但不建议这样做
    ret = Book.objects.all().values("price")
    # < QuerySet[{'price': Decimal('100.00')}, {'price': Decimal('100.00')}, {'price': Decimal('200.00')}] >
    ret = Book.objects.all().values("price","title")
    # < QuerySet[(Decimal('100.00'), 'python红宝书'), (Decimal('100.00'), 'php'), (Decimal('200.00'), 'go')] >
    print(ret)
    print(ret[0].get("price"))

    # 10、value_list()方法，返回的是一个含有元组的列表
    ret = Book.objects.all().values_list("price","title")
    print(ret)
    # <QuerySet [(Decimal('100.00'), 'python红宝书'), (Decimal('100.00'), 'php'), (Decimal('200.00'), 'go')]>

    # 11、distinct 去重，配合着values和value_list使用才有意义
    ret = Book.objects.all().values("price").distinct()
    print(ret)

    # ==================================查询表记录之模糊查询========================================

    ret = Book.objects.filter(price__gt=10,price__lt=200)# price__gt：> 的意思，price__lt: < 的意思，找到 >10的<200的price
    ret = Book.objects.filter(title__startswith="py")# title 中开头是"py"的
    ret = Book.objects.filter(title__contains="h")# title 中含有"h"的
    ret = Book.objects.filter(title__icontains="h")# title 中含有"h"的，不区分大小写
    ret = Book.objects.filter(price__in=[100,200,300])# price里有列表中这几个价格的可以过滤出来
    ret = Book.objects.filter(pub_date__year=2018,pub_date__month=6)# pub_data 里2018年的字段，只有DateFiled的才能这样用
    print(ret)

    # ==================================删除记录和修改记录========================================

    # delete() 调用者：model对象，QuerySet对象
    # ret = Book.objects.filter(price=100).first().delete()
    # ret = Book.objects.filter(price=100).delete() # 返回的是 (2,{'app01.Book':2})，记录删除的个数，一般就是直接删

    # update() 调用者：QuerySet对象
    # ret = Book.objects.filter(title="php").update(title="php_update")# 返回的是修改的个数




    return HttpResponse("OK")
