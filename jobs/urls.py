from django.conf.urls import url
from jobs import views

urlpatterns = [
    # url视图是以joblist开头的，然后跳转到职位列表，name定义的是别名，内部函数比如action={% url '别名'%}就可直接跳转到joblist/
    url(r"^joblist/",views.joblist,name="joblist"),
    url(r"job/(?P<job_id>\d+)/$",views.detail,name="detail"),
]