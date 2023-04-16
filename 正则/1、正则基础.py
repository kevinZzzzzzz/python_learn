"""
正则的三个基础方法
    match，search，findall
    match：匹配规则，匹配成功返回匹配对象，否则返回None
        span() 返回匹配的下标位置范围
        group() 返回匹配的内容
"""
import re
s = 'python itheima pythone itheima python itheime'
result = re.match('python', s)
print(result)
try:
    print(result.span())
    print(result.group())
except:
    pass

"""
search(匹配规则，被匹配字符串)
    搜索整个字符串，找出匹配的，从前向后，找到第一个后，就停止，要是找不到就返回None
"""
s = '1puthon666itheima666python666'
result = re.search('python', s)
print(result)
print(result.span())
print(result.group())



"""
findall(匹配规则，被匹配字符串)
匹配整个字符串，找出全部匹配项，没有匹配返回[]
"""
s = '1python666itheima666python666itheima666python'
result = re.findall('python', s)
result1 = re.findall("itemimae",s)
print(result)
print(result1)