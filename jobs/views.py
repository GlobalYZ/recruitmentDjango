# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from jobs.models import Job,Resume
from jobs.models import Cities,JobTypes
from django.views.generic.edit import CreateView # 这是Django里面通用的编辑的视图
from django.views.generic.detail import DetailView
# 这里把我们自定义的页面能够加进来，Django的视图可以用函数定义，也可以用视图的类去定义，这里用函数作为我们的视图，需注册到URL路径里去
def joblist(request):
    # 定义一个变量，内容从数据库里面取就好了，这里的调用是Django model里面的语法，并且按职位类型排序
    job_list = Job.objects.order_by('job_type')
    print(job_list)
    # 加载模板，用模板的加载器 把joblist.html这个模板加载进来
    # template = loader.get_template('joblist.html')
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
    # return HttpResponse(template.render(context))
    return render(request, 'joblist.html', context)

def detail(request,job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]
    except Job.DoesNotExist:
        raise Http404("Job does not exist")

    return render(request,'job.html',{'job':job})

class ResumeDetailView(DetailView):
    """   简历详情页    """
    model = Resume
    template_name = 'resume_detail.html'

from django.contrib.auth.mixins import LoginRequiredMixin
# 不同于上面的方法视图，这是一个类视图
# 话说Django里只能继承一个类，用了Mixin就可以多继承了
class ResumeCreateView(LoginRequiredMixin, CreateView):
    """    简历职位页面  """
    template_name = 'resume_form.html'
    success_url = '/joblist/' # 创建成功了直接跳转到列表页
    model = Resume
    fields = ["username", "city", "phone",
        "email", "apply_position", "gender",
        "bachelor_school", "master_school", "major", "degree",
        "candidate_introduction", "work_experience", "project_experience"]


    # def post(self, request, *args, **kwargs):
    #     form = ResumeForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #
    #     return render(request, self.template_name, {'form': form})    # def post(self, request, *args, **kwargs):
    #     form = ResumeForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #
    #     return render(request, self.template_name, {'form': form})

    '''get_initial返回一个字典，字典里设置了一些初始的值，应聘信息都往这里传进来'''
    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial[x] = self.request.GET[x]
        print(initial)
        return initial

    '''form_valid验证表单，'''
    def form_valid(self, form):
        self.object = form.save(commit=False)# 验证完成之后保存
        self.object.applicant = self.request.user# 再取到当前表单关联这个简历的对象，再把简历的申请人applicant设置成当前登录用户
        self.object.save()# 再保存，就可以把当前登录用户和简历做一个关联
        return HttpResponseRedirect(self.get_success_url())