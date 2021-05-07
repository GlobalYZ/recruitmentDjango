# coding:utf-8
'''
python的json模块---通用
方法名 参数  介绍      举例                      返回值
dumps obj 对象序列化 json.dumps([1,2])         字符串
loads str 反序列化   json.loads('[1,2,3]')    原始数据类型

python的pickle模块---python专用
方法名 参数  介绍      举例                      返回值
dumps obj 对象序列化 pickle.dumps([1,2])         比特
loads byte 反序列化  pickle.loads('[1,2,3]')    原始数据类型
'''
import  json
def read(path):
    with open(path,'r') as f:
        data = f.read()
    return json.loads(data)# 将data反序列化回来

def write(path,data):
    with open(path,'w') as f:
        if isinstance(data,dict):
            _data = json.dumps(data)# 将data序列化
            f.write(_data)
        else:
            raise TypeError('data is dict')
    return True

data = {'name':'小木','age':18,'top':176}

if __name__ == '__main__':
    # write('test.json',data)# {"name": "\u5c0f\u6728", "age": 18, "top": 176}
    result = read('test.json')
    print(result,type(result))# {'name': '小木', 'age': 18, 'top': 176} <class 'dict'>
    '''拿到的result可以继续操作'''
    result['sex'] = 'boy'
    write('test.json',result)# {"name": "\u5c0f\u6728", "age": 18, "top": 176, "sex": "boy"}