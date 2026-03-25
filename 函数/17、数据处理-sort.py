"""
sorted函数, 对一组数据进行排序，返回一组新数据
语法格式： sorted(可迭代对象， key = 函数, reverse = xxx)
"""

nums = [2, 3, 5, 3, 2, 65, 543, 6, 9]
result = sorted(nums)
print(result)

re2 = sorted(nums, reverse=True)
print(re2)

# 按照字符串长度排序
nums2 = ['python', 'js', 'java']
re3 = sorted(nums2, key=lambda n: len(n))
print(re3)

# 按年龄排序
person = [
    {'name': '张三', 'age': 29, 'gender': '男'},
    {'name': '李四', 'age': 16, 'gender': '男'},
    {'name': '王五', 'age': 22, 'gender': '女'},
    {'name': '赵六', 'age': 32, 'gender': '男'},
    {'name': '梨花', 'age': 23, 'gender': '女'},
    {'name': '孙七', 'age': 1, 'gender': '男'},
]
re4 = sorted(person, key=lambda n: n['age'], reverse=True)
print(re4)