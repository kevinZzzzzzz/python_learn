"""
filter函数：从一组数据中，筛选出符合条件的元素（过滤），并组成一组新数据
语法：filter(过滤函数，可迭代对象)
"""

nums = [10, 20, 30, 40, 50]
result = filter(lambda x: x > 30, nums)
print(result, list(result))

# 筛选成年人
person = [
    {'name': '张三', 'age': 15, 'gender': '男'},
    {'name': '李四', 'age': 16, 'gender': '男'},
    {'name': '王五', 'age': 17, 'gender': '女'},
    {'name': '赵六', 'age': 18, 'gender': '男'},
    {'name': '梨花', 'age': 19, 'gender': '女'},
    {'name': '孙七', 'age': 20, 'gender': '男'},
]

res = filter(lambda x: x['age'] > 16, person)
print(res, list(res))


