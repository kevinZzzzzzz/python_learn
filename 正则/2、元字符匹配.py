"""
字符  功能
.   匹配任意一个字符（除了\n），\.匹配点本身
[]  匹配[]中列举的字符
\d  数字0-9
\D  非数字
\s  空白，空格
\S  非空白
\w  a-z A-Z 0-9 _
\W  非单词字符
"""
import re

s = 'ithimal @@python2 !!666 ##itchaghasd'
result = re.findall(r'\d', s)
result1 = re.findall(r'\D', s)
result2 = re.findall(r'\W', s)
result3 = re.findall(r'[a-zA-Z]', s)
print(result)
print(result1)
print(result2)
print(result3)



# 账号由字母和数字组成，长度限制6-10位
r = '^[0-9a-zA-Z]{6,10}$'
s = '123452s'
print(re.findall(r, s))
# 匹配QQ号，要求纯数字，长度5-11 第一位不为0
r = '^[1-9][0-9]{4,10}$'
s = '012312412'
print(re.findall(r, s))


# 匹配邮箱地址，qq、163、gmail三种邮箱地址
r = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
s = 'jie73680516@qq.com'
print(re.match(r, s))
