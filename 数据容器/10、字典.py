"""
字典的定义，跟集合一样，都是使用{}，不过是以键值对的方式存取,
          不允许重复， key和value可以为任何类型，key不能为字典
    定义字典字面量：
        {key1: value1, key2: value2, ..., keyN: valueN}
    定义字典变量
        my_dict = {key1: value1, key2: value2, ..., keyN: valueN}
    定义空字典
        my_dict = {}
        my_dict = dict()
"""
# 定义字典
my_dict = {"王力宏": 99, '周杰伦': 99, "林俊杰": 90}
my_dict2 = {}
my_dict3 = dict()
print(my_dict, type(my_dict))
print(my_dict2, type(my_dict2))
print(my_dict3, type(my_dict3))

# 定义重复key的字典， 后面声明的会替换前面的
my_dict = {"王力宏": 99, "王力宏": 98, '周杰伦': 99, "林俊杰": 90}
print(my_dict)

# 获取字典内的数据
print(my_dict['王力宏'])
print(my_dict['周杰伦'])
print(my_dict['林俊杰'])

"""
安全取值 若键key不存在，会返回默认值（如果没有设置默认值，则返回None）
"""
result = my_dict.get('haha')
print(result)  # None
result1 = my_dict.get('aghah', '不存在')   # 不存在
print(result1)
# 定义嵌套
my_dict4 = {
    "王力宏": {"yw": 70, 'sx': 90, 'yy': 99},
    "周杰伦": {"yw": 20, 'sx': 30, 'yy': 99},
    "林俊杰": {"yw": 40, 'sx': 50, 'yy': 99}
}
print(my_dict4['王力宏']['yy'])
print(my_dict4['周杰伦']['sx'])
print(my_dict4['林俊杰']['yw'])

"""
字典新增、更新元素
语法：字典[key] = value
"""
my_dict4['张学友'] = {"yw": 90, 'sx': 90, 'yy': 99}
print(my_dict4)
my_dict4['周杰伦']['yw'] = 30
print(my_dict4)

"""
删除元素
语法：字典.pop(key)
"""
my_dict4.pop("王力宏")
print(my_dict4)

"""
清空字典
语法: 字典.clear()
"""
my_dict5 = my_dict4.copy()
my_dict5.clear()
print(my_dict5, my_dict4)

"""
获取全部key
语法：字典.keys()
"""
list1 = my_dict4.keys()
print(list1, type(list1))
for i in list1:
    print(i, my_dict4[i])

"""
遍历字典
"""
for i in my_dict4:
    print(i, my_dict4[i])

"""
统计字典的长度
语法：len(字典)
"""
print(len(my_dict4))

"""
练习：
姓名      部门      工资      级别
王力宏    科技部    3000       1
周杰伦    市场部    5000       2
林俊杰    市场部    7000       3
张学友    科技部    4000       1
对所有级别为1级的员工，上升一级，薪水增加1000
"""
set1 = {
    "王力宏": {"部门": "科技部", "工资": 3000, "级别": 1},
    "周杰伦": {"部门": "市场部", "工资": 5000, "级别": 2},
    "林俊杰": {"部门": "市场部", "工资": 7000, "级别": 3},
    "张学友": {"部门": "科技部", "工资": 4000, "级别": 1}
}
set2 = dict()
for i in set1:
    if set1[i]['级别'] == 1:
        set2[i] = set1[i].copy()
        set2[i]['级别'] += 1
        set2[i]['工资'] += 1000
    else:
        set2[i] = set1[i]
print(set1)
print(set2)
