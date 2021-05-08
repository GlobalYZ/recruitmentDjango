'''
日志的作用，日记，程序行为，重要信息记录，其等级:
debug    帮助我们查看在开发的过程中输出信息是否正确，
info     代表一般的消息类信息，只是为了记录一些程序的行为，比如程序已经执行到了某个位置，进行一些简单的记录
warnning 它是一种警告，一般来说程序不会出错，但是可能有些潜在的风险，可以抛出这种日志信息
error    业务中出现了重大问题，不应该出现的某种情况
critical 更为严重了，一般error就可以了，很少会用到

logging模块的使用
logging.basicConfig
参数名         作用              举例
level     日志输出等级        level=logging.DEBUG
format    日志输出格式
filename  存储位置            filename='d://back.log'
filemode  输入模式            filemode="w"

format具体格式
格式符             含义
%(levelname)s   日志级别名称
%(pathname)s    执行程序的路径
%(filename)s    执行程序名
%(lineno)d      日志的当前行号
%(asctime)s     打印日志的时间
%(message)s     日志信息
'''
# coding:utf-8
import logging
import os


def init_log(path):
    if os.path.exists(path):# 查看这个文件存不存在
        mode = 'a'
    else:
        mode = 'w'
    logging.basicConfig(
        level=logging.INFO,# 定义等级，INFO以下的等级不会被输出，输出等级可以用 logging.大写 来查看
        format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',
        filename=path,
        # filemode='w',# 用w 就不能追加内容了，每次都是覆盖之前的
        filemode=mode,# 写入到上边定义的文件，由于这个文件并不存在，所以用w，如果存在，可以用a，a是可以追加内容的
    )
    return logging

current_path = os.getcwd()
path = os.path.join(current_path, 'back.log')
log = init_log(path)

log.info('这是第一个记录的日志信息')
log.warning('这是一个警告')
log.error('这是一个重大的错误信息')
log.debug('这是一个debug')# 这个不会记录，因为DEBUG等级比较低

