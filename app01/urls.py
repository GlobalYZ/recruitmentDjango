from django.urls import path,re_path
from app01 import views

urlpatterns = [
    re_path(r"^articles/2003/$",views.special_case_2003,name="s_c_2003"),
    # 若要从URL中捕获一个值，只需要在它周围放置一对圆括号()
    # 不需要添加一个前导的反斜杠，因为每个URL都有，例如：应该是^articles，而不是^/articles
    # 每个正则表达式前面的 r 是可选的，但是建议加上，它告诉python这个字符串是“原始的”————字符串中任何字符都不应该转义
    # 匹配规则里只要出现()了，相当于加了一个组，传参时会将其单独传入，下面括号内意思是0-9的数字有四位，用来表示年份的
    re_path(r"^articles/([0-9]{4})/$",views.year_archive,name="y_a"),# year_archive(request,1999)
    # re_path(r"^articles/([0-9]{4})/([0-9]{2})/$",views.month_archive),# month_archive(request,2827,12)
    # 将上面的改造一下，按关键字 ?P 命名来传参，函数里就会根据名字来对应上，但一定要叫y m
    re_path(r"^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$",views.month_archive),# month_archive(request,y=2827,m=12)
    re_path(r"^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$",views.article_detail),

]
# import re
# 前面是匹配规则，^和$符是为了限制首和尾的，后面是待匹配项，
# re.search("^articles/2003/$","articles/2003/")