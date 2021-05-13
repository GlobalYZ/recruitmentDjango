import csv

from django.core.management import BaseCommand
from interview.models import Candidate


class Command(BaseCommand):
    help = '从一个CSV文件的内容中读取候选人列表，导入到数据库中'

    def add_arguments(self, parser):# 定义一个命令行参数
        parser.add_argument('--path',type=str)

    '''
    如果读取的开头出现\ufeff，是由于文件以UTF-8等Unicode格式保存，会在文件头（第一个字符）加入一个BOM（Byte Order Mark）标识。
    它是标记字节顺序的方法。所以可以在后边加上encoding='utf-8-sig',相关查阅https://www.cnblogs.com/mjiang2017/p/8431977.html
    '''
    def handle(self,*args,**kwargs):
        path = kwargs['path']
        with open(path,'rt',encoding='utf-8-sig') as f:
            reader = csv.reader(f,dialect='excel')# 如果报错，可以加上,delimiter=';'这个用;作为的分隔符来读取
            for row in reader:
                canditate = Candidate.objects.create(
                    username=row[0],
                    city=row[1],
                    phone=row[2],
                    bachelor_school=row[3],
                    major=row[4],
                    degree=row[5],
                    test_score_of_general_ability=row[6],
                    paper_score=row[7]
                )
            print(canditate)