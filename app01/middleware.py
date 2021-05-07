
class MyMiddleware:
    def __init__(self,request):
        print("自定义中间件的初始化__init__")

    def process_request(self,request):
        '''产生request对象之后，url匹配之前调用'''
        print("process_request")# 把用户请求信息封装成request对象-------匹配url，查找相应的视图之间

    def process_view(self,request,view_func,*view_args,**view_kwargs):
        '''url匹配之后，视图函数调用之前调用'''
        print("process_view")# 匹配url，查找相应的视图之间-------执行视图中的逻辑代码之间

    def process_response(self,request,response):
        '''视图函数调用之后，内容返回浏览器之前'''
        print("process_response")# 返回HttpResponse对象-------用户之间
        return response# 这里的response一定要返回的，不返回是要出错的
    def process_exception(self,request,exception):
        print(exception)