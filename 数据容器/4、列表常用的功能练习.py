"""
[21,25,21,24,22,20]记录一批学生的年龄
请通过列表的功能对其进行
1、定义列表
2、追加数字31到列表尾部
3、追加一个新的列表[29,33,30]到列表尾部
4、取出第一个元素
5、取出最后一个元素
6、查找31在列表中的位置
"""
ageList = [21, 25, 21, 24, 22, 20]
print(f"1、{ageList}")
ageList.append(31)
print(f'2、{ageList}')
ageList.extend([29, 33, 30])
print(f"3、{ageList}")
num1 = ageList[0]
print(f"4、{num1}")
num2 = ageList[-1]
print(f"5、{num2}")
idx = ageList.index(31)
print(f'6、{idx}')
