# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from jobs.models import Job
from jobs.models import Cities,JobTypes
# 这里把我们自定义的页面能够加进来，Django的视图可以用函数定义，也可以用视图的类去定义，这里用函数作为我们的视图，需注册到URL路径里去
def joblist(request):
    # 定义一个变量，内容从数据库里面取就好了，这里的调用是Django model里面的语法，并且按职位类型排序
    job_list = Job.objects.order_by('job_type')
    print(job_list)
    # 加载模板，用模板的加载器 把joblist.html这个模板加载进来
    template = loader.get_template('joblist.html')
    # 定义上下文
    context = {'job_list':job_list}
    # 然后遍历职位列表，这里不是必须的，因在页面上需要展示城市的名字和职位的类别，这两个在model里是choices类型的，类似枚举型多选择项，
    # 所以我们把职位和城市的类型转成字符串，赋予到job.city_name跟job_type属性，意思是这些属性可以新加出来显示到页面上
    for job in job_list:
        job.city_name = Cities[job.job_city][1]# 从列表中取得值
        job.job_type = JobTypes[job.job_type][1]
        job.fuckName = "这个属性可以随意填写"# 可以直接赋予一个属性，在前端调用显示


    # print(job_list.first().job_city) # 1 ，所以Cities[1][1]得出"上海"
    # 用模板的render方法把上下文展现给用户
    return HttpResponse(template.render(context))

def detail(request,job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]
    except Job.DoesNotExist:
        raise Http404("Job does not exist")

    return render(request,'job.html',{'job':job})
