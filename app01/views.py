from django.shortcuts import render

# Create your views here.
# 视图函数这里必须要传request，它是通过urls文件里的path传过来的
def timer(request):
    import time

    ctime = time.time()
    # 把数据嵌入到html中，只需在第三个参数上传递即可，相当于把变量传递了，html那边的名字是和data保持一致的
    return render(request,"timer.html",{"date":ctime})