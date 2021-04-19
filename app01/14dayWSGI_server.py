from wsgiref.simple_server import make_server

# 请求一旦来了，用下面函数来处理，传入两个参数
def application(environ,start_response):
    # 按着http协议解析数据：environ
    # 按着http协议组装数据：start_response
    print(environ)
    print(type(environ))

    # 当前请求路径
    path = environ.get("PATH_INFO")
    start_response('200 OK',[])# 消息头可有可无[('content-Type','text/html)]

    if path == "/14dayStudy":
        with open("14dayStudy.html","r") as f:
            data = f.read()
    elif path == "/14dayStudyPost":
        print("POST___________________________________")
        with open("14dayStudyPost.html","r") as f:
            data = f.read()
    return [data.encode("utf8")]# wsgi规定的，一定要放字节出去

# 封装socket，返回的是一个类对象
httped = make_server("127.0.0.1",8800,application)

# 等待用户链接：conn,addr = sock.accept()
httped.serve_forever()# application(environ,start_response)