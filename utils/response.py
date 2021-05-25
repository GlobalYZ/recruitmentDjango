from django.http import JsonResponse


class NotFoundJsonResponse(JsonResponse):
    """ 400 对应JSON响应 """
    status_code = 400

    def __init__(self, *args, **kwargs):

        data = {
            "error_code": "404000",
            "error_msg": "您访问的内容不存在或已被删除。"
        }
        super().__init__(data, *args, **kwargs)