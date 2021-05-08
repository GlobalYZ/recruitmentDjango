'''
函数名     参数      介绍          举例                      返回值
md5      byte     Md5算法加密    hashlib.md5(b'hello')      Hash对象
sha1     byte     Sh1算法加密    hashlib.sha1(b'hello')     Hash对象
sha256   byte     Sha256算法加密 hashlib.sha256(b'hello')   Hash对象
sha512   byte     Sha512算法加密 hashlib.sha512(b'hello')   Hash对象
'''
# coding:utf-8
import hashlib
import time

base_sign = "muke"  # A与B要达成共识的一个--基础签名

def custom():
    a_timestamp = int(time.time())# A这个要生成凭证字符串的--时间戳
    _token = '%s%s' % (base_sign,a_timestamp)# 定义一个加密之前的token，通过格式化将二者导入
    # print(_token)# muke1620353840
    hashobj = hashlib.sha1(_token.encode('utf-8'))# 要传入的类型是byte，设置一下utf-8的字符格式
    a_token = hashobj.hexdigest()# 生成16进制的一个加密串
    # print(a_token)# 7a156153c502b2bb2f13cec5027188c4c0a6dca7
    return a_token, a_timestamp # 原来return是支持多个值进行返回的，用，隔开就行，收取的时候也一样

def b_service_check(token,timestamp):
    _token = '%s%s' % (base_sign,timestamp)
    b_token = hashlib.sha1(_token.encode('utf-8')).hexdigest()
    if token == b_token:
        return True
    else:
        return False

if __name__ == '__main__':
    need_help_token, timestamp = custom()# 如果只用一个变量来收取，那么将以元组的形式都给它
    result = b_service_check(need_help_token,timestamp)
    if result:
        print("a合法，b服务可以进行帮助")
    else:
        print("a不合法，b不可进行帮助")

