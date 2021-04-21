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