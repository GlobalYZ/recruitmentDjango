'''
yaml文件可以在服务启动之前读取，将一些配置信息放入到我们的服务中，进行初始化
python的第三方模块---pyyaml
pip install PyYAML
import yaml
'''
import yaml
# coding:utf-8

def read(path):
    with open(path,'r') as f:
        data = f.read()
    result = yaml.load(data,Loader=yaml.FullLoader)# 加上Loader会更安全
    return result

if __name__ == '__main__':
    result = read('muke.yaml')
    print(result,type(result))
    # {'url': 'https://www.imooc.com/', 'types': ['前沿', '前端', '后端', '移动端', '云计算', '运维', 'ui'], 'python': {'web': 'django', 'spader': 'bs5'}} <class 'dict'>
    print(dir(yaml))# 查询yaml的方法

