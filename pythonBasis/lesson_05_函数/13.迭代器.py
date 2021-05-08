# coding:utf-8

iter_obj = iter((1,2,3))
print(next(iter_obj))# 1
print(next(iter_obj))# 2
print(next(iter_obj))# 3
# print(next(iter_obj)) 抛出异常

def _next(iter_obj):
    try:
        return next(iter_obj)
    except StopIteration:
        return None

iter_obj = iter((1,2,3))
print(_next(iter_obj))# 1
print(_next(iter_obj))# 2
print(_next(iter_obj))# 3
print(_next(iter_obj))# None

iter_obj = iter((1,2,3))
for i in iter_obj:
    print(i)

def make_iter():
    for i in range(10):
        yield i
iter_obj = make_iter()
print(type(iter_obj))# <class 'generator'> 是迭代器类型的


iter_obj = (i for i in range(10))
for i in iter_obj:
    print(i)
for i in iter_obj:# 注意：上边已经读过了之后，内存放空了，这个就读不了了
    print(i)
