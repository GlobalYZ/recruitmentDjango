from django.conf.urls import url
from jobs import views

urlpatterns = [
    # url视图是以joblist开头的，然后跳转到职位列表
    url(r"^joblist/",views.joblist,name="joblist")
]