'''
async定义异步
await执行异步
asyncio调用async函数
函数名             介绍                  参数                      返回值
gather      将异步函数批量执行       asyncfunc...           List函数的返回结果
run         执行主异步函数          【task】                 执行函数的返回结果

async def main():
    result = await asyncio.gather(
        a(),    # a和b函数也是经过async定义了的
        b()
    )
    print(result)
if __name__ == '__main__':
    asyncio.run(main())


还有一个实现异步的方式：gevent模块，下面是常用方法：
函数名             介绍                  参数          返回值
spawn       创建协程对象          Func，args           协程对象
joinall     批量处理协程对象       [spawnobj]           [spawnobj]


'''

# coding:utf-8
import asyncio
import os
import random
import time
import gevent

def gevent_a():
    for i in range(10):
        print(i,'a gevent',os.getpid())
        gevent.sleep(random.random() * 2)# 这里的sleep属于业务的阻塞

    return 'gevent a result'

def gevent_b():
    for i in range(10):
        print(i,'b gevent',os.getpid())
        gevent.sleep(random.random() * 2)

    return 'gevent b reasult'

async def a():
    for i in range(10):
        print(i,'a',os.getpid())
        # time.sleep(random.random() * 2)# 每次返回一个0~1的随机数字(有小数) * 2
        await asyncio.sleep(random.random() * 2)# time.sleep属于CPU级别的阻塞，使用它会吃去异步效果，这里的sleep属于业务的阻塞
    return 'a function'

async def b():
    for i in range(10):
        print(i,'b',os.getpid())
        # time.sleep(random.random() * 2)
        await asyncio.sleep(random.random() * 2)
    return 'b function'

async def main():
    result = await asyncio.gather(
        a(),
        b()
    )
    print(result[0],result[1])

if __name__ == '__main__':
    start = time.time()
    # asyncio.run(main())
    g_a = gevent.spawn(gevent_a)
    g_b = gevent.spawn(gevent_b)
    gevent_list = [g_a,g_b]
    result = gevent.joinall(gevent_list)
    print(result)# [<Greenlet at 0x103ed26a0: _run>, <Greenlet at 0x103d82370: _run>] 返回的是协程对象
    print(result[0].value)# gevent a result

    print(time.time() - start)
    print('parent is %s' % os.getpid())