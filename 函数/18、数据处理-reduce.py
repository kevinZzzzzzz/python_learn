"""
reduce函数，将一组数据不断合并，最终归并成一个结果
语法格式：reduce(合并函数， 可迭代函数， 初始值)
备注：reduce函数需要从 functools 模块中引入才能使用
"""
from functools import reduce

nums = [1, 2, 3, 4, 5]
result = reduce(lambda x, b: x + b, nums)
print(result)
 