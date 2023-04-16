"""
单例模式的优点
    对一个类只获取其唯一一个类示例对象，并且持续复用它
    节省内存
    节省创建对象的开销
"""

class strTool():
    pass

s1 = strTool()
s2 = strTool()
# s1 != s2
print(s1, id(s1))
print(s2, id(s2))

from str_tools import str_tools
s3 = str_tools
s4 = str_tools
# s3 != s4
print(s3, id(s3))
print(s4, id(s4))