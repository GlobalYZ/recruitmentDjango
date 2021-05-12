'''
进程池的创建-multprocessing:进程池中的进程不会被关闭，可以反复使用
函数名             介绍                  参数                  返回值
Pool            进程池创建           Processcount       进程池对象
apply_async   任务加入进程池（异步）   func,args           无
close          关闭进程池                无              无
join            等待进程池任务结束         无             无

进程锁的加锁与解锁
from multiprocessing import Manager
manager = Manager()
lock = manager.Lock()
函数名         介绍          参数          返回值
acquire     上锁             无           无
release     开锁（解锁）      无           无

'''

# coding:utf-8
import multiprocessing
import os
import time


def work(count,lock):
    lock.acquire()# 书写这一步，代表它下面就是加锁大门的内部了，在同一时间只能对一个进程进行开发
    print(count,os.getpid())
    time.sleep(5)
    lock.release()# 这一步就解锁了，说明他走出大门了
    # return 'result is %s,pid is %s' % (count,os.getpid())


if __name__ == '__main__':
    pool = multiprocessing.Pool(5)# 代表创建的进程池里有5个进程
    manger = multiprocessing.Manager()
    lock = manger.Lock()
    results = []
    for i in range(20):
        result = pool.apply_async(func=work,args=(i,lock))
        results.append(result)

    # for res in results:
    #     print(res.get())# 能返回每一个apply_async的回值，只要它拥有,并且通过这种方式也不需要调用close()和join()也能正常执行

    # 因为pool进程池也是主进程的一部分，主进程迅速结束了，它也就跟着关闭了，所以要做一个延迟才可以体现出子进程的状态
    # time.sleep(20)

    pool.close()
    pool.join()