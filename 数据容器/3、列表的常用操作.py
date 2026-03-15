"""
查找某元素下标
功能：查找指定元素在列表的下标，如果找不到，报错ValueError
语法：列表.index(元素)
"""
myList = ['haha', 'hsa2sd', '2e2wqe']
idx = myList.index('hsa2sd')
print('hsa2sd在列表中的下标索引值是：', idx)
# 如果查找的元素不存在，则报错
# index = myList.index(123)  # ValueError: 123 is not in list
# print(index)


"""
修改特定位置的元素值
语法：列表[下标]=值
"""
myList = ['haha', 'hsa2sd', '2e2wqe']
myList[0] = 'hsa2sd'
print(myList)
myList[-1] = 'h22424242'
print(myList)

"""
在指定位置追加元素
语法：列表.insert(指定位置，元素)
"""
# 插入
myList.insert(0, 'kevinZzzzz')
print(myList)

"""
在尾部插入元素
语法：列表.append(元素)，将指定元素，追加到列表的为尾部
语法2：列表.extend() 追加一批元素
"""
myList.append('wos kevinsxsxsx')
print(myList)
myList.append([21, 2, 321, 3])
print(myList)

myList.extend([1, 2, 3, 4])
print(myList, 1231)

"""
删除元素
语法1: del 列表[下标]
语法2: 列表.pop(下标)
"""
del myList[0]
del myList[1]
print(myList)
delEle = myList.pop(3)
print(myList, '删除的元素:', delEle)

"""
删除某元素在列表中的第一个匹配项
语法：列表.remove(元素)
"""
myList.remove('h22424242')
print(myList)

"""
清空列表
语法：列表.clear()
"""
myList1 = [1, 2, 3, 4, 5]
myList1.clear()
print(myList1)

"""
统计某元素在列表内的数量
语法：列表.count(元素)
"""
mylis1 = [1, 2, 3, 1, 2, 3, 4, 5]
num = mylis1.count(1)
print(num)

"""
统计列表内的全部元素数量
语法：len(列表）
"""
print(len(mylis1))
print(len(myList))
print(len(myList1))

"""
获取容器内所有数的总和
必须是数字类型
语法：sum(列表)
"""
result1 = sum([1, 2, 3, 4, 5, 6])
print(result1)
