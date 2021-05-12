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
        yield i# yield相当于是个return ,下次再进来从这次的值之后开始,只要有yield的函数就是generator类型了，带send()函数，send()里带next()
iter_obj = make_iter()
print(type(iter_obj))# <class 'generator'> 是生成器类型


iter_obj = (i for i in range(10))# 这样也是生成一个迭代器类型
print(type(iter_obj))# <class 'generator'>
print(list(iter_obj))#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in iter_obj:
    print('i = ',i)# 注意：如果上边已经读过了之后，内存放空了，这个就读不了了

iter_obj = [i*i for i in range(10)]
print(type(iter_obj))# <class 'list'> 不同于上面的()，他是列表类型
print(iter_obj)
print(iter_obj)
