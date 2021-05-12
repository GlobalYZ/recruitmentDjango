'''
进程的创建模块--multiprocessing
函数名         介绍              参数           返回值
Process     创建一个进程      target，args     进程对象
start       执行进程            无               无
join        阻塞程序            无               无
kill        杀死进程            无               无
is_alive    进程是否存活         无               bool

'''

# coding:utf-8
import multiprocessing
import os
import time


def work_a():
    for i in range(10):
        print(i,'a',os.getpid())# os.getpid()进程号
        time.sleep(1)
def work_b():
    for i in range(10):
        print(i,'b',os.getpid())
        time.sleep(1)
if __name__ == '__main__':
    start = time.time()
    a_p = multiprocessing.Process(target=work_a)
    # a_p.start()
    b_p = multiprocessing.Process(target=work_b)
    # b_p.start()
    for p in (a_p,b_p):
        p.start()
    for p in (a_p,b_p):
        p.join()# 阻塞，a_p和b_p执行完再往下执行
    for p in (a_p,b_p):
        print(p.is_alive())# False False

    print('时间的消耗是：', time.time()-start)
    print('parent pid is %s' % os.getpid())
