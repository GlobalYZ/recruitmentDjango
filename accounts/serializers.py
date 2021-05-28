from utils.serializers import BaseSerializer


class UserSerializer(BaseSerializer):
    """ 用户的基础信息 """
    def to_dict(self):# 重写
        user = self.obj
        return {
            'username': user.username,
            'nickname': user.nickname,
            'avatar': user.avatar_url,# 头像地址
            'email': user.email,
        }


class UserProfileSerializer(BaseSerializer):
    """ 用户的详细信息 """
    def to_dict(self):
        profile = self.obj
        return {
            'real_name': profile.real_name,
            'sex': profile.sex,# 返回0或1
            'sex_display': profile.get_sex_display(),# 这个方法会返回对应的sex的中文信息，方便理解
            'age': profile.age,
        }
