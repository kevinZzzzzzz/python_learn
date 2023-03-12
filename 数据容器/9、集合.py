"""
集合的定义
    定义集合字面量：{元素1，元素2，。。。，元素n}
    定义集合变量：变量名称 = {元素1， 元素2， 元素3，。。。。， 元素n}
    定义空集合：变量名称 = set()
集合的性质
    集合是无序的，所以不支持下标索引
    集合和列表一样是允许修改的
"""
# 定义一个集合
my_set = {'haha', 'hehe', 'enen', 'haha', 'hehe', 'enen'}
my_set_empty = set()
print(f"my_set的内容是：{my_set}，类型是：{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty}, 类型是：{type(my_set_empty)}")

"""
添加新元素
语法：集合.add(元素)    
"""
my_set = {'hello', 'world'}
my_set.add('hahaha')
print(my_set)
my_set.add('hello')  # 去重
print(my_set)

"""
移除元素
语法：集合.remove(元素)
"""
my_set.remove('hello')
print(my_set)

"""
随机取出一个元素
语法：集合.pop()
"""
my_set = {1, 2, 3, 4, 5}
ele = my_set.pop()
print(f"随机取出：{ele}", my_set)

"""
清空集合
语法：集合.clear()
"""
my_set = {1, 2, 3, 4, 5}
my_set.clear()
print(my_set)

"""
取出两个集合的差集
语法:集合1.difference(集合2)（集合1里面有的 集合2里面没有的）
不会修改原来的集合
"""
my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}
my_set3 = my_set1.difference(my_set2)
print(my_set3)

"""
消除2个集合的差集
语法：集合1.difference_update(集合2)
在集合1内消除集合2相同的元素
结果：集合1被修改，集合2不变
"""
my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}
my_set1.difference_update(my_set2)
print(my_set1, my_set2)

"""
集合的合并
语法：集合1.unior(集合2)
将集合1和集合2组成新的集合，包括去重
结果得到新的集合，集合1和集合2不变
"""
my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}
my_set3 = my_set1.union(my_set2)
print(my_set1, my_set2, my_set3)


"""
统计集合的数量
语法：len(集合)
"""
my_set1 = {1, 2, 3, 1, 2, 3, 4}
print("集合的长度：", len(my_set1))

"""
集合遍历
"""
my_set1 = {1, 2, 3, 1, 2, 3, 4}
for i in my_set1:
    print(i)
