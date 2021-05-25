from django.db import models

from utils.models import CommonModel


class User(CommonModel):
    """ 用户模型 """
    username = models.CharField('用户名', max_length=32, unique=True)
    password = models.CharField('密码', max_length=256)
    avatar = models.ImageField('用户头像', upload_to='avatar/%Y%m', null=True, blank=True)
    nickname = models.CharField('昵称', max_length=32, unique=True)

    class Meta:
        db_table = 'account_user'
