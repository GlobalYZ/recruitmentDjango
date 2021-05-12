'''
队列的创建-multiprocessing
函数名         介绍          参数              返回值
Queue       队列的创建       nam_cout        队列对象
put         信息放入队列      message         无
get         获取队列信息      无               str

'''

# coding:utf-8
import json
import multiprocessing
import time


class Work(object):
    def __init__(self,q):
        self.q = q

    def send(self,message):
        if not isinstance(message,str):# 如果message不是字符串类型
            message = json.dumps(message)# 将message传入
        self.q.put(message)

    def receive(self):
        while True:
            result = self.q.get()
            try:
                res = json.loads(result)
            except:
                res = result
            print('recv is %s' % res)

    def send_all(self):
        for i in range(20):
            self.q.put(i)
            time.sleep(1)

if __name__ == '__main__':
    q = multiprocessing.Queue()
    work = Work(q)
    send = multiprocessing.Process(target=work.send,args=({'name':'小木'},))
    recv = multiprocessing.Process(target=work.receive)
    send_all_p = multiprocessing.Process(target=work.send_all)

    send_all_p.start()
    send.start()
    recv.start()

    send_all_p.join()
    recv.terminate()# 终结接收端