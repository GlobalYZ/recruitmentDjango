from django.contrib import admin
from app01.models import *
# Register your models here.
# 用来自定制Admin下的展示
class AccountAdmin(admin.ModelAdmin):
    list_display = ('username','email','signature')
    search_fields = ('username','email')# 可搜索字段
    list_filter = ('email',)# 右边栏可过滤的字段，注意：即便有一个字段也要加","，以元组的形式
    list_editable = ['signature',]# 在外直接就能编辑了
    list_per_page = 5# 默认展示数量

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','account','read_count','get_tags')
    search_fields = ('title',)  # 可搜索字段
    list_filter = ('account','pub_date')
    # list_display_links = ['account',]# 可以修改成 点别的 来进入修改，没啥卵用
    # fields = ('title','content',('pub_date','read_count'))# 显示哪些属性，并且把什么字段放在一行显示
    # exclude = ('read_count','tags')# 不显示什么字段，与上边会有冲突
    # radio_fields = {'account':admin.HORIZONTAL}# 将下拉选改为圆扭选择
    # raw_id_fields = ['account',]# 将外键字段设置成需要点开选择的，并显示成在数据库的数字ID，
    readonly_fields = ('read_count',)# 将字段改为 只读
    autocomplete_fields = ['account',]# 自动补全，很适合外键
    date_hierarchy = 'pub_date'# 在外展示时可以按日期来分组，只能按日期来，只有这一个字段
    fieldsets = (   # 用这个修饰字段会和fields冲突，只能用其一
        ('文章内容',{
            'fields':['title','content','account'],
            'classes':('wide','extrapretty'),# 调整 好看的 样式，没什么卵用
        }),(
            '发布相关',{
                'classes':('collapse',),# 会有一个"显示/隐藏"按钮
                'fields':('pub_date','tags','read_count')
            }
        )
    )
    filter_horizontal = ('tags',)# 只能针对"多对多"，会增加一个选择框，横向的
    # filter_vertical = ('tags',)# 竖向的

class TagAdmin(admin.ModelAdmin):
    list_display = ['name','colored_name','color_code',]
    list_editable = ['color_code',]# 在外直接就能编辑了


# admin.site.register(Books)
# admin.site.register(Publish)
# admin.site.register(Author)
# admin.site.register(AuthorDetail)

admin.site.register(Account,AccountAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Tag,TagAdmin)
