import  socket
# 模拟写服务器的简单代码，要基于socket来做


sock = socket.socket() # 创建socket
sock.bind(("127.0.0.1",8800))# 绑定一个服务器地址和端口
sock.listen(5)# 最大排队数

while 1:
    print("server waiting...")
    conn,addr = sock.accept()# 等待用户来链接，两个变量，conn是客户端的套接字，是浏览器自己封装的套接字对象，addr
    # http协议是基于请求响应，客户端浏览器发了一堆字符串，包含了各种数据，url，get or post 等。
    data = conn.recv(1024)# 按照固定格式接收了一些信息，所有的请求信息都在data里
    print("data ",data)# 如果有能把data里收到的请求数据以字典或者对象的形式处理好的办法，------dict/obj data={“path”：“/login”}

    # 就可以data.get(path)
    # 按着http请求协议请求数据
    # 专注web业务开发
    # path = data.get("path")
    # if path == "/login":
    #     return login.html
    # 按着http响应协议封装数据

    # 读取html文件
    with open("14dayStudyPost.html","rb") as f:
        data = f.read()
    print("data ", data)

    conn.send((b"HTTP/1.1 200 OK\r\n\r\n%s"%data))
    # 需要统一发字节串
    # conn.send(("HTTP/1.1 200 OK\r\n\r\n%s"%data).encode("utf8"))
    # HTTP/1.1 200 OK是响应首行，前面应该有响应头，可写可不写，固定格式\r\n\r\n隔开后面的是页面内容的响应体
    # conn.send(b"HTTP/1.1 200 OK\r\n\r\nhello Yang")# 不论请求的是什么，暂时发送一个字符串,HTTP/版本 响应状态码成功 文本解释OK与200并行
    conn.close()# 断开连接，一次请求结束就断开连接，不会一直挂着，等待下一次

'''
data  b'GET /favicon.ico HTTP/1.1\r\n
Host: 127.0.0.1:8800\r\n
Connection: keep-alive\r\n
sec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"\r\n
sec-ch-ua-mobile: ?0\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36\r\n
Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8\r\n
Sec-Fetch-Site: same-origin\r\n
Sec-Fetch-Mode: no-cors\r\n
Sec-Fetch-Dest: image\r\n
Referer: http://127.0.0.1:8800/\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: zh-CN,zh;q=0.9\r\n\r\n'

GET请求没有请求体，只有POST有请求体
请求首行\r\n
请求头\r\n
请求头\r\n
请求头\r\n\r\n
请求体
\r\n\r\n之后才是请求体

GET请求提交的数据会放在URL之后，你？分割URL和传输数据，参数之间以&相连，如Editbook?name=test1&id=123456.
POST方法是把提交的数据放在HTTP包的请求体中。
GET提交的数据大小有限制（因为浏览器对URL的长度有限制），而POST方法提交的数据没有限制。
GET与POST请求在服务端获取请求数据方式不同。

URL：四部分
协议：//IP：端口(80)/路径？a=1&b=2

data  b'POST / HTTP/1.1\r\n
Host: 127.0.0.1:8800\r\n
Connection: keep-alive\r\n
Content-Length: 44\r\n
Cache-Control: max-age=0\r\n
sec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"\r\n
sec-ch-ua-mobile: ?0\r\n
Upgrade-Insecure-Requests: 1\r\n
Origin: http://127.0.0.1:8800\r\n
Content-Type: application/x-www-form-urlencoded\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n
Sec-Fetch-Site: same-origin\r\n
Sec-Fetch-Mode: navigate\r\n
Sec-Fetch-User: ?1\r\n
Sec-Fetch-Dest: document\r\n
Referer: http://127.0.0.1:8800/\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: zh-CN,zh;q=0.9\r\n\r\n
user=%E7%94%A8%E6%88%B7%E5%90%8D&pwd=mima123'

'''