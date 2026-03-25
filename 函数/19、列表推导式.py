"""
列表推导式： 用一条简洁语句，从可迭代对象中，生产新列表的语法结构
备注：列表推导式本质上是对 for循环 + append() 的一个简写形式
语法：[表达式 for 变量 in 可迭代对象]
"""

# 需求: 让列表中的每个元素，都变为原来的两倍，得到是一个新的列表
# 方式一
nums = [10, 20, 30, 40]
re1 = map(lambda x: x * 2, nums)
print(tuple(re1))

# 方法二
re2 = []
for i in nums:
    re2.append(i * 2)
print(re2)

# 方式3
re3 = [i * 2 for i in nums]
print(re3)

# 带条件的列表推导式
re4 = [n * 2 for n in nums if n > 20]
print(re4)

# 字典推导式
names = ['张三', '李四', '王五']
scopes = [60, 70, 80]
# {'张三': 60, '李四': 70, '王五': 80}
re5 = {names[n]: scopes[n] for n in range(len(names))}
print(re5)