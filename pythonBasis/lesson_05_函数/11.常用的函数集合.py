'''
函数名             参数                   介绍                  返回值         举例
abs             Number          返回数字绝对值                 正数字         abs(-10)
all             List            判断列表内容是否全是true         Bool         all(['','123'])
help            object          打印对象的用法                 无            help(list)
enumerate       iterable        迭代时记录索引                 无             for index,item in enumerate(list)
input           Str             命令行输入消息                 Str            input('请输入信息')
isinstance      Object,type     判断对象是否是某种类型           Bool          isinstance('a',str)
type            Object          判断对象的类型                 Str             type(10)
vars            instance        返回实例化的字典信息             dict
dir             object          返回对象中所有可用方法和属性      List           dir('asd')
hasattr         Obj,key         判断对象中是否有某个属性         Bool           hasattr('1','upper')
setattr         Obj,key,value   为实例化对象添加属性和值          无             setattr(instance,'run','go')
getattr         Obj,key         通过对象获取属性                任何类型        getattr(obj,key)
any             Iterable        判断内容是否有true值            Bool            any([1,0,''])
'''
# coding:utf-8
python = ['django','flask','tornado']
for index,item in enumerate(python):# enumerate枚举函数可以这样用，同时输出了索引
    print(index,item)

# help(input)
# help(list)
# food = input('你想吃什么呢：')
# print(food)


class Test(object):
    a = 1
    b = 2
    def __init__(self):
        self.a = self.a
        self.b = self.b

test = Test()
print(vars(test))# {'a': 1, 'b': 2}
print(hasattr(test,'a'))# True
print(hasattr(list,'append'))# True
setattr(test,'c',3)
print(vars(test))# {'a': 1, 'b': 2,'c': 3}
# setattr(list,'c','0') 添加的时候会报错，setattr只支持自定义的添加一些属性

if hasattr(list,'append'):
    # 为如果没有属性，会直接报错，所以最好这样加判断来使用
    print(getattr(list,'append'))# <method 'append' of 'list' objects>
else:
    print("不存在这个属性")

a = ['',None,True,0]
print(any(a))# True
# all -> and
# any -> or

