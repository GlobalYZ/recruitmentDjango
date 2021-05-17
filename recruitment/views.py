from django.http import HttpResponse


def page_500(request):
    '''500错误页面'''
    return HttpResponse('服务器正忙，请稍后重试')