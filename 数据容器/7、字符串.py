"""
同元组一样，字符串是一个无法修改的数据容器
因此不能修改，移除，追加字符操作
"""
my_str = 'ahahah kevin asdad'
# 通过下标索引取值
value = my_str[0]
value2 = my_str[-1]
print(value, value2)

# index 查找元素下标
index = my_str.index('h')
print(index)

# replace 替换方法
print(my_str)
my_str = my_str.replace('hahah', 'ah')
print(my_str)

# split 分割方法
# 按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
# 字符串本身不变，而是得到一个列表对象
list1 = my_str.split(' ')
print(list1, type(list1))  # ['aah', 'kevin', 'asdad'] <class 'list'>

# strip() 字符串规整操作  类似js 字符串的trim()
str1 = ' 我企鹅 我企鹅去 请问我去 '
print(str1.strip())  # '我企鹅 我企鹅去 请问我去'
str1 = '12我企鹅 我企鹅去 请问我去21'
str2 = str1.strip('12')  # '我企鹅 我企鹅去 请问我去'
print(str2)


# count() 统计字符串中某字符串出现的次数
num = str1.count('我')
print(f"我出现的次数:{num}")

# len() 统计字符串的长度
print(len(str1))
