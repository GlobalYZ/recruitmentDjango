'''
函数介绍删除了，只介绍lambda：
定义一个轻量化的函数
即用即删除，很适合需要完成一项功能，但是此功能只在此一处使用
无参数：
f = lambda : value  其中value自带返回值效果
f()
有参数：
f = lambda x,y: x*y
f(3,4)

'''
# coding:urf-8

f = lambda: 1
print(f())# 1
f = lambda x,y:x + y
print(f(1,2))# 3
f = lambda x=1,y=2:x + y
print(f())# 3   可以设置默认值，不传参，如果有参没有默认值，一定要在前，例：lambda x,y=2: x+y
f = lambda x,y=2: x > y
print(f(1))# False

users = [
    {'name': 'dewei'},
    {'name': 'xiaomu'},
    {'name': 'asan'},
]
users.sort(key=lambda x:x['name'])
print(users)# [{'name': 'asan'}, {'name': 'dewei'}, {'name': 'xiaomu'}]