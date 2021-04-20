# HttpResponse()是响应对象，（响应首行，消息头，响应体），Django已经帮做好首行和消息头，这里只需加入字符串的响应体
#
from django.shortcuts import render,HttpResponse

# Create your views here.
# 视图函数这里必须要传request，它是通过urls文件里的path传过来的
from django.urls import reverse


def timer(request):
    import time

    ctime = time.time()
    # render()方法给封装好了，填入timer。html会自动去templates文件夹下去找
    # 把数据嵌入到html中，只需在第三个参数上传递即可，相当于把变量传递了，html那边的名字是和data保持一致的
    return render(request,"timer.html",{"date":ctime})

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