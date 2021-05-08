'''
高阶函数
接收函数作为参数，或者将函数作为返回值的函数是高阶函数
filter用法：filter(func,list)
func：对list每个item进行条件过滤的定义
list：需要过滤的列表
map用法：map(func,list)
func：对list每个item进行条件满足的判断
list：需要过滤的列表
reduce用法：reduce(func,list)
func：对数据累加的函数
list：需要处理的列表

'''
# 比如想过滤一下列表中的3的倍数，要这么写函数，很麻烦
from functools import reduce

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def fn(func, lst):
    new_list = []
    for n in lst:
        # 判断n的奇偶
        if func(n):
            new_list.append(n)
    return new_list
def fn4(i):
    return i % 3 == 0
print(fn(fn4 , l))# [3, 6, 9]

# filter()可以从序列中过滤出符合条件的元素，保存到一个新的序列中
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = filter(lambda i: i > 5, l)
print(list(r))# [6, 7, 8, 9, 10]

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# map()函数可以对可迭代对象中的所有元素做指定的操作，然后将其添加到一个新的对象中返回
r = map(lambda i: i ** 2, l)
print(list(r))# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 注意：reduce函数，对字符串来讲，是可以做累加的，就是合并到了一起，但不能用累乘，会报错，不做举例了
res = reduce(lambda x,y: x+y,[0,1,2])# 3
res = reduce(lambda x,y: x*y,[1,2,3,4])# 24
print(res)# 24

# sort()方法用来对列表中的元素进行排序，它是直接比较列表中的元素的大小
# 在sort()可以接收一个关键字参数 ，key，key需要一个函数作为参数
l = ['bb', 'aaaa', 'c', 'ddddddddd', 'fff']
l.sort(key=len)
print(l)# ['c', 'bb', 'fff', 'aaaa', 'ddddddddd']

l = [2, 5, '1', 3, '6', '4']
l.sort(key=int)
print(l)# ['1', 2, 3, '4', 5, '6']

# sorted()这个函数和sort()的用法基本一致，可以对任意的序列进行排序，排序不会影响原来的对象，而是返回一个新对象
l = [2, 5, '1', 3, '6', '4']
# l = "123765816742634781"

print('排序前:', l)# [2, 5, '1', 3, '6', '4']
print(sorted(l, key=int))# ['1', 2, 3, '4', 5, '6']
print('排序后:', l)# [2, 5, '1', 3, '6', '4']
