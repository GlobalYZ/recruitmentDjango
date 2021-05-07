# 开箱即用
# 为了实现开箱即用的思想，Python中为我们提供了一个模块的标准库
# 在这个标准库中，有很多很强大的模块我们可以直接使用，
#   并且标准库会随Python的安装一同安装
# sys模块，它里面提供了一些变量和函数，使我们可以获取到Python解析器的信息
#   或者通过函数来操作Python解析器
# 引入sys模块
import sys

# pprint 模块它给我们提供了一个方法 pprint() 该方法可以用来对打印的数据做简单的格式化
import pprint

# sys.argv
# 获取执行代码时，命令行中所包含的参数
# 该属性是一个列表，列表中保存了当前命令的所有参数
# print(sys.argv)

# sys.modules
# 获取当前程序中引入的所有模块
# modules是一个字典，字典的key是模块的名字，字典的value是模块对象
# pprint.pprint(sys.modules)

# sys.path
# 他是一个列表，列表中保存的是模块的搜索路径
# ['C:\\Users\\lilichao\\Desktop\\resource\\course\\lesson_06\\code',
# 'C:\\dev\\python\\python36\\python36.zip',
# 'C:\\dev\\python\\python36\\DLLs',
# 'C:\\dev\\python\\python36\\lib',
# 'C:\\dev\\python\\python36',
# 'C:\\dev\\python\\python36\\lib\\site-packages']
# pprint.pprint(sys.path)

# sys.platform
# 表示当前Python运行的平台
# print(sys.platform)

# sys.exit()
# 函数用来退出程序
# sys.exit('程序出现异常，结束！')
# print('hello')

# os 模块让我们可以对操作系统进行访问
import os

# os.environ
# 通过这个属性可以获取到系统的环境变量
# pprint.pprint(os.environ['path'])

# os.system()
# 可以用来执行操作系统的名字
# os.system('dir')
# os.system('notepad')

'''
os的文件与目录函数介绍
函数名     参数              介绍                              举例                          返回值
getcwd    无             返回当前的路径                      os.getcwd()                     字符串
listdir   path          返回指定路径下所有的文件或文件夹       os.listdir('c://Windows')      返回一个列表
makedirs  Path mode     创建多级文件夹                      os.makedirs('d://imooc/py')        无
removedirs path         删除多级文件夹                      os.removedirs('d://imooc/py')      无
rename    Oldname       给文件或文件夹改名                   os.rename('d://imoos;,'d://imoc')  无
rmdir     path          只能删除空文件夹                    os.rmdir('d://imooc')              无

os.path模块常用方法
函数名     参数              介绍                    举例                     返回值
exists   Path           文件或路径是否存在     os.path.exists('d://')        bool类型
isdir    Path           是否是路径            os.path.isdir('d://')         bool类型
isabs    Path           是否是绝对路径         os.path.isabs('test')         bool类型  
isfile   Path           是否是文件            os.paht.isfile('d://a.py')    bool类型
join     Path,path*     路径字符串合并         os.path.join('d://','test')   字符串
split    Path           以最后以层路径为基准切割 os.path.split('d://test')     列表
'''
# coding:utf-8

current_path = os.getcwd()
print(current_path)# /Users/globalyz/Desktop/recruitment/pythonBasis/lesson_06_对象/code
# new_path = '%s/test1/test2' % current_path
# os.makedirs(new_path)# 当前目录下创建一个test1的文件夹，后面如果还有，就联级创建
# data = os.listdir(current_path)
# print(data)

# os.removedirs('test1/abc')# 联级删除两个文件夹，没有路径则报错
# os.rename('test1','test1_new')# 没有路径则报错
# os.rename('m.py','m_new'.py)# 改文件的名字
# os.rmdir('test1')# 只能删除空的文件夹，不然报错

new_path2 = os.path.join(current_path,'test1','abc')
print(new_path2)# /Users/globalyz/Desktop/recruitment/pythonBasis/lesson_06_对象/code/test1/abc
# split功能会把最后一层与前面的进行分割
print(os.path.split(current_path))# ('/Users/globalyz/Desktop/recruitment/pythonBasis/lesson_06_对象', 'code')

print(dir(os.path))

'''
sys中的常用方法
函数名      参数         介绍                  举例           返回值
modules    无      Py启动时加载的模块    sys.modules()         列表
path       无      返回当前py的环境路径   sys.path()           列表
exit       arg     退出程序             sys.exit(0)          无
getdefaultencoding
           无      获取系统编码        sys.getdifaultencoding() 字符串
platform   无      获取当前系统平台     sys.platform()          字符串
version(属性) 无    获取python版本     sys.version             字符串
argv      *args    程序外部获取参数     sys.argv              列表
'''

modules = sys.modules
print(sys.path)
# sys.exit(1)# 进程已结束，退出代码为 1
print(sys.argv)