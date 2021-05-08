'''
random.random
随机返回0~1之间的浮点数
random.uniform
产生一个a、b区间的随机浮点数
random.randint
产生一个a、b区间的随机正数
random.choice
返回对象中的一个随机元素
random.sample
随机返回对象中指定的元素
random.randrange
获取区间内的一个随机数
'''
import random

print(random.random())# 0.963807146537485
print(random.uniform(1,10))# 8.772193091483578
print(random.randint(1,10))# 8
print(random.choice(['a','b','c']))# c
print(random.choice('abc'))# b
print(random.sample(['a','b','c'],2))# ['c', 'b']  返回了指定数量为2的元素个数
print(random.sample('abc',2))# ['a', 'c']   注意，Sample返回的都是列表
print(random.randrange(0,100,1))# 51
'''相当于下面的语句，用range生成一个步长为1的列表，然后从中返回一个随机数'''
print(random.choice(range(0,100,1)))


gifts = ['iphone','ipad','car','tv']
def choice_gifts():
    gift = random.choice(gifts)
    print('你得到了%s' % gift)

def choice_gif_new():
    count = random.randrange(0,100,1)
    if 0 <= count <= 50:
        print('你中了一个iphone')
    elif 50 < count <= 70:
        print('你中了一个ipad')
    elif 70 < count < 90:
        print('你中了一个tv电视')
    elif count >= 90:
        print('恭喜你中了一辆小汽车')


if __name__ == '__main__':
    choice_gif_new()