# 直接赋值： 两个变量指向同一个对象，修改其中一个，会影响另外一个
# num1 = [1, 2, 3, 4]
# num2 = num1
# num1[2] = 10
#
# print(num1)
# print(num2)

import copy

"""
浅拷贝
创建一个新的外层容器，但内部元素仍然引用原来的对象
from copy import copy
"""
num1 = [1, 2, 3, 4]
num3 = copy.copy(num1)

num1[2] = 10
print(num1)  # [1, 2, 10, 4]
print(num3)  # [1, 2, 3, 4]
"""
浅拷贝存在的问题
嵌套数据仍然存在共享的，修改嵌套的数据会相互影响
"""
num4 = [1, 2, 3, [4, 5]]
num5 = copy.copy(num4)
num5[3][0] = 10
print(num4)  # [1, 2, 3, [4, 10]]
print(num5)  # [1, 2, 3, [4, 10]]

"""
深拷贝
创建一个新的外层容器，并对其内部所有的【可变子对象】进行递归复制
"""
num6 = [1, 2, 3, [4, 5]]
num7 = copy.deepcopy(num6)
num6[3][0] = 10
print(num6)
print(num7)

# 深拷贝只复制可变对象，不可变对象会直接引用
# 元组中如果只包含不可变对象，则深拷贝无效


