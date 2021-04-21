# 自定义过滤器和标签
from django import template

register = template.Library()# register是固定名称
@register.filter
def multi_filter(x,y):
    return x * y

@register.simple_tag
def multi_tag(x,y,z):
    return x * y * z