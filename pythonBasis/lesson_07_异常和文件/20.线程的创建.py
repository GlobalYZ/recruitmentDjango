'''
线程的创建---threading
方法名         说明                  举例
Thread      创建线程        Thread(target,args)
线程对象的方法
start       启动线程            start()
join        阻塞直到线程执行结束  join(timout=None)
getName     获取线程的名字       getName()
setName     设置线程的名字       setName(name)
is_alive    判断线程是否存活      is_alive()
setDaemon   守护线程            setDaemon(True)


'''

# coding:utf-8
import random
import threading
import time

lists = ['python','django','tornado','flask','bs5','requests','uvloop']

new_lists = []

def work():
    if len(lists) == 0:
        return
    data = random.choice(lists)
    lists.remove(data)
    new_data = '%s_new' % data
    new_lists.append(new_data)
    time.sleep(1)

if __name__ == '__main__':
    start = time.time()
    print('old list len:',len(lists))
    t_list = []
    for i in  range(len(lists)):
        t = threading.Thread(target=work)
        t_list.append(t)
        t.start()

    for t in t_list:
        t.join()

    print('old list:',lists)
    print("new list:",new_lists,len(new_lists))
    print('time is %s' % (time.time() - start))