'''
线程池---concurrent
futures.ThreadPoolExecutor      创建线程池       tpool = ThreadPoolExecutor(max_workers)
线程池对象的方法
submit      往线程池中加入任务   submit(target,args)
done        线程池中的某个线程是否完成了任务        done()
result      获取当前线程执行任务的结果           result()

'''

# coding:utf-8
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor

lock = threading.Lock()

def work(i):
    # lock.acquire()
    print(i,os.getpid())
    time.sleep(1)
    # lock.release()
    return 'result is %s' % i

if __name__ == '__main__':
    print('主进程 :',os.getpid())
    t = ThreadPoolExecutor(2)# 给线程池加入两个任务
    result = []
    for i in range(20):
        t_result = t.submit(work,(i,))
        result.append(t_result)

    for res in result:
        print(res.result())



