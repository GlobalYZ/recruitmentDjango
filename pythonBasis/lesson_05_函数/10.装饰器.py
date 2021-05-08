from functools import wraps
from textwrap import wrap
# 希望函数可以在计算前，打印开始计算，计算结束后打印计算完毕
#  我们可以直接通过修改函数中的代码来完成这个需求，但是会产生以下一些问题
#   ① 如果要修改的函数过多，修改起来会比较麻烦
#   ② 并且不方便后期的维护
#   ③ 并且这样做会违反开闭原则（OCP）
#           程序的设计，要求开发对程序的扩展，要关闭对程序的修改
def out_one(fun):
    def inter_one(*args , **kwargs):
        print('out_one开始执行~~~~')
        # 调用被扩展的函数
        result = fun(*args , **kwargs)
        if result == 10: print('result is %s' % result)
        print('out_one执行结束~~~~')
        return result
    return inter_one

# 像out_one()这种函数我们就称它为装饰器
# 通过装饰器，可以在不修改原来函数的情况下来对函数进行扩展
# 在开发中，我们都是通过装饰器来扩展函数的功能的
# 在定义函数时，可以通过@装饰器，来使用指定的装饰器，来装饰当前的函数
# 可以同时为一个函数指定多个装饰器，这样函数将会按照从内向外的顺序被装饰

def out_two(fun):
    def inter_two(*args , **kwargs):
        print('out_two~开始执行~~~~')
        # 调用被扩展的函数
        result = fun(*args , **kwargs)
        if result == 10: print('result is %s' % result)
        print('out_two~执行结束~~~~')
        return result
    return inter_two

@out_two
@out_one
def say_hello(data):
    return data

print('下面是根据runoob上学来的验证函数本身的调用类型type，在没加@wrap的包裹下，产生了函数内调用的类型，非本身类型')
say_hello(10)
print(say_hello.__name__)# inter_two ，也就是say_hello()这个函数实际引用地址已经是inter_two的了，每包一层就会变一层
