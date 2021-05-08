# 通过类型检查，可以检查只能值（变量）的类型

a = 123 # 数值
b = '123' # 字符串

# print('a =',a)
# print('b =',b)、

# type()用来检查值的类型
# 该函数会将检查的结果作为返回值返回，可以通过变量来接收函数的返回值
c = type('123')
c = type(a)
print(type(b))# <class 'str'>
print(type(1)) # <class 'int'>
print(type(1.5)) # <class 'float'>
print(type(True)) # <class 'bool'>
print(type('hello'))  # <class 'str'>
print(type(None)) # <class 'NoneType'>

test = 123
print("test type= ",type(test))# test type=  <class 'int'>
print("test id= ",id(test))# test id=  2187506571440
test = "变成字符串"
print("test = ",type(test))# test =  <class 'str'>
print("test id= ",id(test))# test id=  2187513565424




