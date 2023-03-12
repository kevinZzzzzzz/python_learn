"""
    列表 基本语法：
    字面量[元素1，元素2，元素3，。。。]
    定义变量
    变量名称 = [元素1，元素2，元素3，。。。]
    定义空列表
    变量名称 = []
    变量名称 = list()
"""
name_list = ['hahaha', 3333, True]
print(name_list)
print(type(name_list))

# 嵌套列表
my_list = [['haha', 2213], ['ahasd', 213]]
print(my_list)
print(type(my_list))

# 列表的下标索引
print(name_list[0])
print(my_list[0][1])
# 下标反向
print(name_list[-1])
