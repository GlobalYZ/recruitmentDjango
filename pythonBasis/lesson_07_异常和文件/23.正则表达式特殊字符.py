'''
正则表达式中的常用特殊字符
特殊字符    描述
\d      匹配任何十进制数字，与[0~9]一致
\D      匹配任意非数字
\w      匹配任何字母数字下划线字符
\W      匹配非字母数字及下划线
\s      匹配任何空格字符，与[\n\t\r\v\f]相同
\S      匹配任意非空字符
\A      匹配字符串的起始
\Z      匹配字符串的结束
.       匹配任何字符（除了\n之外）

'''

# coding:utf-8

import re
def had_number(data):
    result = re.findall('\d',data)

