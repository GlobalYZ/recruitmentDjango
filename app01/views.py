import datetime

from django.http import JsonResponse, FileResponse, HttpResponseRedirect

from app01.models import *
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
import time
# HttpResponse()是响应对象，（响应首行，消息头，响应体），Django已经帮做好首行和消息头，这里只需加入字符串的响应体

'''类视图 一继承视图django.views.generic.TemplateView，二，配置模板地址，三，配置URL。TemplateView是继承了三个类。
使用class改写视图实际上是面向对象改造的过程，Django内置的通用视图使代码更精简'''
class HomeView(TemplateView):
    template_name = 'home.html'# 可直接返回模板，无需render

def search(request):
    '''
    请求对象就一个request实例，响应对象可以有多种类型
    HttpResponseBase
        |--HttpResponse (文本)
            |--JsonResponse
            |--HttpResponseRedirect (重定向)
        |--StreamingHttpResponse (二进制流)
            |--FileResponse
    '''
    name = request.GET.get('name','')# 可以理解成类似于字典，查询name的值，如果没有，给它一个空值
    print(name)# 浏览器输入http://127.0.0.1:8000/app01/search/?name=1，取得值 1

    print(request.method)# GET POST
    print(request.GET,request.POST)# QueryDict的字典对象，可以根据request.GET.get("name")取值
    print(request.path)# /app01/search/    url:协议：//IP：port/路径？请求数据，，，打印的是端口号之后，？之前的路径
    print(request.get_full_path)# 区别于上边，全打印出来
    print(request.build_absolute_uri())# 绝对路径,括号里可以输入字符串，它能自动拼接上 http://127.0.0.1:8000/app01/search/?name=1
    print(request.scheme)# 请求是http还是https
    print(request.content_type)# text/plain意思是文本，有各种类型的回复
    print(request.COOKIES)# cookie信息 {'csrftoken': 'WRCI54tFKHdDzZHdhYAwaTkxPz4AXpFNvAx8S8Ts2YUSGR8wv7QPgOJNrhO8o6Lu', 'sessionid': '907obfjomggho274kip23u79bmxt1ggg'}
    print(request.FILES)# 文件信息
    print(request.META)# 请求头信息，里面有很多的数据，以JSON字典的形式存储。比如： REMOTE_ADDR-请求的IP地址，HTTP——USER_AGENT-请求用户的终端信息
    print(request.headers)# 精简了META

    resp = HttpResponse('响应内容',status=201)
    resp.status_code = 204# 再改也可以
    user_info = {
        'name': '张三',
        'age': 34
    }

    # return resp
    # return JsonResponse(user_info)
    resf = FileResponse(open('medias/huluwa.jpeg','rb'))
    return resf

def no_data_404(request):
    return HttpResponse('404访问的页面不存在')

def article_detail(request, article_id):
    '''文章详情，ID是从1000开始的整数，如果没有，重定向到404，article_id: 文章ID'''
    if article_id < 1000:
        # return HttpResponseRedirect('/app01/not/found/')# 这种方法不太推荐
        return redirect('/app01/not/found/')# 注意，传入的no_data_404是视图函数的名称(我没成功)
    return HttpResponse('文章{}的内容: '.format(article_id))

def special_case_2003(request):
    # 反向解析，给一个别名，通过reverse可解析出地址，在任意函数中都可以调用,加上命名空间更精准
    url = reverse("app01:s_c_2003")#
    print("url命名空间:    -------      ",url)# url命名空间:    -------       /app01/articles/2003/
    # 如果解析地址中含正则表达式，则需要传入一个符合该正则表达式的任意值代理匹配才可以
    url = reverse("app01:y_a",args=(7788,))# r"^articles/([0-9]{4})/$"
    print("url:    -------      ",url)# url:    -------       /app01/articles/7788/
    html = "一些返回的网页内容"
    res = HttpResponse(html,content_type="text/plain",status=404)# 也可以在这里修改返回的类型，状态码等
    res.reason_phrase = "状态码加上这个标签"
    # return res
    return HttpResponse("special_case_2003")

def year_archive(request,year):
    return HttpResponse(year)

def month_archive(request,y,m):
    return HttpResponse(y + "  " + m)

def path_year(request,year):
    print(type(year))# 输出类型是<class 'int'>，得益于主urls里的有名分组，否则将是字符串类型
    return HttpResponse("path_year```")
def path_month(request,month):
    print(type(month))# <class 'int'>
    return HttpResponse("path_month```: {}".format(month))

def index(request):
    '''
    模板语法：两种情况
    ① 变量    {{  }}
       1. 涉及到深度查询,用句点符
       2. 涉及到数据转换，用过滤器      {{val|filter_name:参数}}
    ② 标签    {%  %}
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
    now = datetime.datetime.now()
    person_List = []
    file_size = 1231423423
    text = "hello python hi luffycity go java linux"
    user = "洋哥"
    # user = None
    date = time.time()
    # return render(request,"timer.html",{"date":ctime})
    return render(request,"timer.html",locals())# 由于变量名多，一一写入麻烦，可以用locals()方法将其一起传入，但名字要对应一致

def mysqlIndex(request):
    # ==================================添加表记录========================================
    # 方式一
    # book_obj = Book(id=1,title="python红宝书",price=100,pub_date="2020-12-12",publish="洋哥出版社")
    # book_obj.save()

    # 方式二 creat返回值就是当前生成的这条对象记录
    # id因为已设置成自增，故可以不传，此方式会直接执行后边的创建，返回给book_obj，无需save，
    # book_obj = Book.objects.create(title="php",price=100,pub_date="2020-12-18",publish="洋哥出版社")
    # book_obj = Book.objects.create(title="python", price=200, pub_date="2021-12-18", publish="洋哥出版社")
    # print(book_obj.title)
    # print(book_obj.price)
    # print(book_obj.pub_date)

    # 补充，如果是多对多的对象，创建时不需要对ManyToMany的字段赋值，等创建完了，再用对象.多对多的字段.set([?,?])
    # 例如：o = Article(title=...) --- o.tags.set([1,2]) --- 如果再次 o.tags.set([1,]) 那么将是重新赋值的意思，2就对应着没了
    #   如果是原有记录上加新，要用 o.add(3,4)        解释：这里的1234对应的都是Tag类里的id

    # ==================================查询表记录API========================================
    '''
    1 方法的返回值
    2 方法的调用者

    '''
    # 1、all()方法，返回值是一个queryset对象，queryset是支持切片的，但只支持正切片
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
    # 补充，如果想.reverse()反转排序，必须先要经过order_by()排序才可以使用

    # 7、count() 调用者：QuerySet，返回值：int
    ret = Book.objects.all().count()
    print(ret)

    # 8、exist() 这样实际调用会使用LIMIT 1，随意查看一条语句，只要有存在则返回True，比直接all()要快很多，all()相当于select *
    ret = Book.objects.all().exists()
    if ret:
        print("OK")

    # 9、values()方法，可以直接循环取每一个对象的特有字段，返回的是一个含有字典的QuerySet列表，调用者：QuerySet，返回值：QuerySet
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
    # <QuerySet [{'price': Decimal('100.00'), 'title': 'php'}, {'price': Decimal('200.00'), 'title': 'python'}, {'price': Decimal('100.00'), 'title': 'go'}]>
    print(ret)
    print(ret[0].get("price"),"-----------------------------")

    # 10、value_list()方法，返回的是一个含有元组的列表
    ret = Book.objects.all().values_list("price","title")
    print(ret)
    # <QuerySet [(Decimal('100.00'), 'python红宝书'), (Decimal('100.00'), 'php'), (Decimal('200.00'), 'go')]>

    # 11、distinct 去重，配合着values和value_list使用才有意义
    ret = Book.objects.all().values("price").distinct()
    print(ret)

    # ==================================查询表记录之模糊查询========================================

                                                         # 大于等于是__gte
    ret = Book.objects.filter(price__gt=10,price__lt=200)# price__gt：> 的意思，price__lt: < 的意思，找到 >10的<200的price
    ret = Book.objects.filter(title__startswith="py")# title 中开头是"py"的，大小写敏感，istartswith 大小写不敏感
    ret = Book.objects.filter(title__contains="h")# title 中含有"h"的   大小写敏感，title__icontains 大小写不敏感
    ret = Book.objects.filter(title__endswith="h")  # title 中结尾"h"的，不区分大小写 iendswith大小姐不敏感
    ret = Book.objects.filter(price__in=[100,200,300])# price里有列表中这几个价格的可以过滤出来
    # ret = Account.objects.filter(register_date__range=['2018-01-30',datetime.date(2018,5,20)]) range：区间查询
    ret = Book.objects.filter(pub_date__year=2018,pub_date__month=6)# pub_data 里2018年的字段，只有DateFiled的才能这样用
    print(ret)

    # ==================================删除记录和修改记录========================================

    # delete() 调用者：model对象，QuerySet对象
    # ret = Book.objects.filter(price=100).first().delete()
    # ret = Book.objects.filter(price=100).delete() # 返回的是 (2,{'app01.Book':2})，记录删除的个数，一般就是直接删

    # update() 调用者：QuerySet对象
    # ret = Book.objects.filter(title="php").update(title="php_update")# 返回的是修改的个数

    return HttpResponse("OK")

def  add(request):
    # pub = Publish.objects.create(name="人民出版社",email="123@139.com",city="北京")
    # ----------------------------绑定一对多的关系---------------------------------------------------
    # 方式一：建议用
    # 为book表绑定出版社： ① publish ———— 多 books
    # books_obj = Books.objects.create(title="红楼梦",price="100",publishDate="2012-12-12",publish_id=1)
    # 方式二：也可以，相当于给翻译过来了
    # pub_obj = Publish.objects.filter(nid=1).first()
    # books_obj = Books.objects.create(title="西游记", price="100", publishDate="2012-12-12", publish=pub_obj)
    # print(books_obj.publish)# Publish object (1)    与这本书籍关联的出版社对象，如果需要显示出来内容，在各种class里加上__str__
    # print(books_obj.publish.name,books_obj.publish.email,books_obj.publish_id)# 都能点出来
    # 比如，查询西游记的出版社对应的邮箱
    # books_obj = Books.objects.filter(title="西游记").first()
    # print(books_obj)# Books object (4)  如有__str__  那么：西游记
    # print(books_obj.publish)  # Publish object (1)  如有__str__  那么：人民出版社
    # print(books_obj.publish.email)# 123@139.com
    # --------------------------------绑定多对多的关系----------------------------------------------
    # books_obj = Books.objects.create(title="金瓶梅", price="100", publishDate="2012-12-12", publish_id=1)
    # alex = Author.objects.get(name="alex")# 可以通过get找到Author的model对象，通过对象能拿到主键
    # egon = Author.objects.get(name="egon")# get什么都可以，这里只是好理解用了name
    # 因为多对多的第三张表是ORM生成给数据库的，并没有实际类，所以无法直接操纵，但Django给我们提供了一个接口
    # books_obj.authors.add(alex,egon)# 绑定多对多关系的API，用类属性里的多对多字段，直接点add，这样写会自动去找alex和egon的主键
    # books_obj.authors.add(1,2,4)# add(*[1,2,4]) 这两种是如果已知Author主键，也可以直接写定，后者是python的一种语法，等效位置参数

    # 解除多对多关系API
    books_obj = Books.objects.filter(nid=9).first()
    # books_obj.authors.remove(2)# books_obj.authors.remove(*[1,2]) 写法一样
    # books_obj.authors.clear()# 将nid=9的书籍在多联集表中全部清除

    print(books_obj.authors.all())# QuerySet:与这本书关联的所有作者对象



    return HttpResponse("ok")


def query(request):
    '''
    跨表查询：
        1 基于对象查询（子查询）
        2 基于双下划线查询（Join查询）
        3 聚合和分组查询
        4 F 与 Q查询
    :param request:
    :return:
    '''
    # -----------------------------------基于对象的跨表查询（子查询）-----------------------------
    '''
    A-B两个表，无论是一对一，一对多，还是多对多，关联属性在A表中
    正向查询：A------>B  按字段
    反向查询：B------>A  按表名，表名小写_set.all()  是个QuerySet
    # 一对多查询：
                                通过 books_obj.publish 正向查询
            Books（关联属性：publish）------------------> Publish
                                通过 publish_obj.books_set.all() 反向查询
    '''
    # 一对多的正向查询：查询金瓶梅这本书的出版社的名字
    books_obj = Books.objects.filter(title="金瓶梅").first()
    print(books_obj.publish)# 与这本书关联的出版社对象
    print(books_obj.publish.name)
    # 一对多的反向查询：查询人民出版社出版过的书籍名称
    publish_obj = Publish.objects.filter(name="人民出版社").first()
    ret = publish_obj.books_set.all()
    # 等同于下面
    publish_obj = Publish.objects.get(name="人民出版社")
    ret = publish_obj.books_set.select_related()# all和select_related效果是一样的
    print(ret)


    '''
    正向查询：A------>B  按字段
    反向查询：B------>A  按表名，表名小写_set.all()  是个QuerySet
    # 多对多查询：
                                通过 books_obj.authors.all() 正向查询
            Books（关联属性：authors）------------------> Author
                                通过 author_obj.books_set.all() 反向查询
    '''
    # 多对多查询的正向查询：查询金瓶梅这本书的作者的名称
    books_obj = Books.objects.filter(title="金瓶梅").first()
    author_list = books_obj.authors.all()# QuerySet对象  [author_obj,author_obj`````]
    for author in author_list:
        print(author.name)
    # 多对多查询的反向查询：查询alex出版过的所有书籍名称
    author_obj = Author.objects.filter(name="Alex").first()
    books_list = author_obj.books_set.all()
    for books in books_list:
        print(books.title)


    '''
    正向查询：A------>B  按字段
    反向查询：B------>A  按表名小写
    # 一对多查询：
                                    通过  author_obj.authordetail 正向查询
            Author（关联属性：authordetail）------------------> AuthorDetail
                                    通过  authordetail_obj.author 反向查询
    '''
    # 一对一查询的正向查询：查询alex的手机号
    author_obj = Author.objects.filter(name="alex").first()
    authordetail_obj = author_obj.authordetail
    print(authordetail_obj.telephone)
    # 一对一的反向查询：查询手机号为110的作者的名字和年龄
    authordetail_obj = AuthorDetail.objects.filter(telephone="110").first()
    author_obj = authordetail_obj.author
    print(author_obj.name)


    # ----------------------------------------基于双下划线的跨表查询（Join查询）----------------------
    '''
    基于双下划线的跨表查询（Join查询）
        key:正向查询：按字段 values("关联字段__查询字段")
            反向查询：按表名小写__"字段名称" values("查询字段")
    '''
    # 一对多查询的正反向查询：查询金瓶梅这本书的出版社的名字
    # SELECT app01_publish.name FROM app01_book INNER JOIN app01_publish ON app01_book.publish_id = app01_publish.nid WHERE app01_book.title = "金瓶梅"
    # values相当于就是Join，publish是字段，publish__name是orm的特殊语法，可以publish__Publish表的不同字段
    ret = Books.objects.filter(title="金瓶梅").values("publish__name")
    print(ret)# <QuerySet [{'publish__name': '人民出版社'}]>
    ret = Publish.objects.filter(books__title="金瓶梅").values("name")
    print(ret)

    # 多对多的正反向查询：查询金瓶梅这本书的所有作者的名字（Join）
    # 通过Books表Join与其关联的Author表，属正向，按字段authors通知ORM引擎join books_author与author
    ret = Books.objects.filter(title="金瓶梅").values("authors__name")
    print(ret)# QuerySet[{},{}]
    # 通过Author
    ret = Author.objects.filter(books__title="金瓶梅").values("name")
    print(ret)# QuerySet

    # 一对一查询正反向查询：查询ales的手机号
    ret = Author.objects.filter(name="alex").values("authordetail__telephone")
    print(ret)# <QuerySet [{'authordetail__telephone': 110}]>
    ret = AuthorDetail.objects.filter(author__name="alex").values("telephone")
    print(ret)# <QuerySet [{'telephone': 110}]>

    # --------------------------进阶练习：---------------------------------------------
    # 手机号以110开头的作者出版过的所有书籍名称以及书籍出版社名称
    # 需求：通过Books表Join AuthorDetail表，Books与AuthorDetail无关联，所以必须连续跨表  PS：下面不加startswith貌似也行
    ret = Books.objects.filter(authors__authordetail__telephone__startswith="110").values("title","publish__name")
    print(ret)# <QuerySet [{'title': '金瓶梅', 'publish__name': '人民出版社'}, {'title': '金瓶梅', 'publish__name': '人民出版社'}]>
    ret = Author.objects.filter(authordetail__telephone__startswith="110").values("books__title","books__publish__name")
    print(ret)

    # 要对方的值时就__
    # 我自我总结一下，filter(里就是过滤的条件).values(里是想要的值的字段)，字段不在表里的就用关联字段或者小写表名__一下

    # ------------------------聚合与分组查询---------------------------------------------

    # -------------------------聚合:aggregate：返回值是一个字典，不再是QuerySet
    from django.db.models import Avg,Max,Min,Count
    # 查询所有书籍的平均价格
    ret = Books.objects.all().aggregate(avg_price=Avg("price"),max_price=Max("price"))# Avg前面可以自定义字典的名字avg_pric
    print(ret)# {'price__avg': Decimal('309.666667')}  //  改名后 {'avg_price': Decimal('309.666667')}

    # -------------------------分组：annotate，返回值依然是QuerySet

    # 单表分组查询
    # 示例1：查询每一个部门的名称以及员工的平均薪水
    ret = Emp.objects.values("dep").annotate(avg_salary=Avg("salary"))
    print(ret)# <QuerySet [{'dep': '教学部', 'avg_salary': Decimal('51000.000000')}, {'dep': '保安部', 'avg_salary': Decimal('5000.000000')}]>
    # 单表分组查询的ORM语法：单表模型.objects.values("group by的字段").annotate(聚合函数("统计字段"))

    # 示例2：查询每一个省份的名称以及员工数
    ret = Emp.objects.values("province").annotate(c_t=Count("id"))
    print(ret)# <QuerySet [{'province': '山东省', 'c_t': 2}, {'province': '河北省', 'c_t': 1}]>

    # 补充知识点
    # ret = Emp.objects.all()
    # print(ret)# select * from emp
    # ret = Emp.objects.values("name")
    # print(ret)# select name from emp


    # 多表分组查询
    # 示例3：查询每一个出版社的名称以及出版的书籍个数
    ret = Publish.objects.values("name").annotate(c_t=Count("books__title"))
    print(ret)# <QuerySet [{'name': '人民出版社', 'c_t': 9}, {'name': '天津出版社', 'c_t': 0}, {'name': '北京出版社', 'c_t': 0}, {'name': '南京出版社', 'c_t': 0}]>

    # 示例4：查询每一个作者的名字以及出版过的书籍的最高价格
    ret = Author.objects.values("name").annotate(max_price=Max("books__price"))
    print(ret)# <QuerySet [{'name': 'alex', 'max_price': Decimal('150.00')}, {'name': 'egon', 'max_price': Decimal('150.00')}]>
    # 跨表的分组查询模型：每一个后表模型.objects.values("name/id").annotate(聚合函数(关联表__统计字段))

    # 示例5：查询每一个书籍的名称以及对应的作者个数
    ret = Books.objects.values("title").annotate(c_t=Count("authors__name"))
    print(ret)# <QuerySet [{'title': '红楼梦', 'c_t': 0}, {'title': '三国演义', 'c_t': 0}, {'title': '西游记', 'c_t': 0}, {'title': '金瓶梅', 'c_t': 3}]>


    # ---------------------------------F查询与Q查询--------------------------------------------
    from django.db.models import F,Q
    # 查询评论数大于阅读数的字段
    ret = Books.objects.filter(comment_num__gt=F("read_num"))
    print(ret)# <QuerySet [<Books: 红楼梦>, <Books: 三国演义>, <Books: 西游记>, <Books: 西游记>]>

    # 把所有的书籍价格都提高1块钱
    # ret = Books.objects.all().update(price=F("price")+1)
    # print(ret)# 9

    # 把书名红楼梦并且价格是100的书籍查出来，下面这种写法是普通写法，"，"代表且的关系，但如果是"或"的话，就要用到Q了
    # ret = Books.objects.filter(title="红楼梦",price=100)
    ret = Books.objects.filter(Q(title="红楼梦")|Q(price=101))# 语法上有"|"，"&"和~Q，代表"非"，如果同时使用键值对，加在Q后边
    print(ret)

    return HttpResponse("OK")

    #   ---------------------------------类视图Class Based Views---------------------------
class classView(View):
    time = datetime.datetime.now()
    def get(self,request):
        return HttpResponse("Class view get request %s" %self.time)
    def post(self,request):
        return HttpResponse("Class view post")
class classView2(classView):# 继承
    time = 10# 覆盖了上面的time 值


    # 中间件
def testMiddleware(request):
    return HttpResponse("testMiddleware OK")