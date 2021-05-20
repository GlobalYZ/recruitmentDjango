from django.urls import path,re_path
from app01 import views
from app01.views import mysqlIndex, add, query, path_month, special_case_2003, year_archive, month_archive, \
    HomeView, search, no_data_404, article_detail, index, books_list_paginator, BooksListView

urlpatterns = [
    path('search/', search,name='search'),  # 这里介绍了request能获取的相关值和response的返回方式
    path('not/found/',no_data_404, name= 'no_data_404'),
    path('article/<int:article_id>/',article_detail,name= 'article_detail'),
    path('mysqlindex/', mysqlIndex),
    path('add/', add),  # 数据库添加
    path('query/', query),  # 数据库查询
    # path("articles/<int:month>", views.path_month),
    # 改造一下上边的月份，限定在1~12,<month>对应视图函数里参数month,名称要保持一致
    path('books/list/paginator/', books_list_paginator, name='books_list_paginator'),# 分页查询
    path('books/list/class/', BooksListView.as_view(), name='books_list_class'),# 分页查询
    re_path(r'^articles/(?P<month>0?[1-9]|1[012])/$',path_month,name='path_month'),
    re_path(r"^index/", index,name="index"),# 这里介绍了如何传递变量到模板
    re_path(r"^articles/2003/$",special_case_2003,name="s_c_2003"),
    # 若要从URL中捕获一个值，只需要在它周围放置一对圆括号()
    # 不需要添加一个前导的反斜杠，因为每个URL都有，例如：应该是^articles，而不是^/articles
    # 每个正则表达式前面的 r 是可选的，但是建议加上，它告诉python这个字符串是“原始的”————字符串中任何字符都不应该转义
    # 匹配规则里只要出现()了，相当于加了一个组，传参时会将其单独传入，下面括号内意思是0-9的数字有四位，用来表示年份的
    re_path(r"^articles/([0-9]{4})/$",year_archive,name="y_a"),# year_archive(request,1999)
    # re_path(r"^articles/([0-9]{4})/([0-9]{2})/$",views.month_archive),# month_archive(request,2827,12)
    re_path(r"^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$",month_archive),# month_archive(request,y=2827,m=12)

    # 调用类视图
    path('home/', HomeView.as_view(), name='home'),  # HomeView类视图里提供了as方法，直接调用类视图
    path('classview/', views.classView.as_view()),  # 调用类视图，GET和POST等请求自动找到对应的方法
    path('classview2/', views.classView2.as_view()),  # 调用继承的类视图
]