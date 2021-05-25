from django.conf.urls import url
from pythonBasis.jobs import views
from django.urls import path

urlpatterns = [
    # url视图是以joblist开头的，然后跳转到职位列表，name定义的是别名，内部函数比如action={% url '别名'%}就可直接跳转到joblist/
    url(r"^joblist/", views.joblist, name="joblist"),

    # 职位详情
    url(r"job/(?P<job_id>\d+)/$", views.detail, name="detail"),

    # 提交简历
    path('resume/add/', views.ResumeCreateView.as_view(), name='resume-add'),
    path('resume/<int:pk>/', views.ResumeDetailView.as_view(), name='resume-detail'),
    # 首页自动跳转到 职位列表
    url(r"^$", views.joblist, name="name"),
]