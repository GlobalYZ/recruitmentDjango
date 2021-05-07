'''
函数名                参数          介绍          举例                               返回值
encodestring        Byte      进行base64加密   base64.encodestring(b'py')           Byte
decodingstring      Byte      对base64解密     base64.decodestring(b'eGlhb211\n')   Byte
encodebytes         Byte      进行base64加密   base64.encodebytes(b'py')            Byte
decodingbytes       Byte      对base64解密     base64.decodebytes(b'eGlhb211\n')    Byte
'''
# coding:utf-8
import base64

replace_one = '%'
replace_two = '$'

def encode(data):
    '''加密'''
    if isinstance(data,str):
        data = data.encode('utf-8')# encode 用于将str类型转换成byte 类型
    elif isinstance(data,bytes):
        data = data
    else:
        raise TypeError('data need bytes or str')
    # return base64.encodebytes(data).decode('utf-8')
    _data = base64.encodebytes(data).decode('utf-8')
    _data = _data.replace('a',replace_one).replace('2',replace_two)# 如果_data里有 a ，那么用replace_one替换，接着一样的链式操作
    return _data


def decode(data):
    '''解密'''
    if not isinstance(data,bytes):
        raise TypeError('data need bytes')
    replace_one_b = replace_one.encode('utf-8')
    replace_two_b = replace_two.encode('utf-8')
    data = data.replace(replace_one_b,b'a').replace(replace_two_b,b'2')
    return base64.decodebytes(data).decode('utf-8')


if __name__ == '__main__':
    result = encode('hello xiaomu')
    print(result)# aGVsbG8geGlhb211  如果返回值没有加.decode('utf-8')，那么返回的就是比特类型，为：b'aGVsbG8geGlhb211\n'
    # 替换后成为了%GVsbG8geGlhb$11，所以需要自定义解密

    new_result = decode(result.encode('utf-8'))
    print(new_result)# hello xiaomu

