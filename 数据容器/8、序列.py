"""
序列是指：内容连续，有序，可以使用下标索引的一类数据容器
列表、元组，字符串都可以视为序列
"""

"""
    序列切片
    语法：序列[起始下标:结束下标:步长]
    起始下标：从何处开始，可以留空表示从头开始
    结束下标：何处结束(不含)，可以留空，表示截取至最末
    步长：表示截取的间距，可以为负数表示反向取,默认步长为1
"""
my_list = [0, 1, 2, 3, 4, 5, 6]
result1 = my_list[1:4]
print(my_list, 'my_list')
print(f'结果1：{result1}')
result11 = my_list[::-1]
print(f"取反结果:{result11}")
result111 = my_list[3:1:-1]
print(f"结果 :{result111}")

my_tuple = (0, 1, 2, 3, 4, 5, 6)
result2 = my_tuple[::3]
print(f"结果2：{result2}")
result22 = my_tuple[::-1]
print(f"取反结果:{result22}")

my_str = '0123456'
result3 = my_str[1::2]
print(f"结果3: {result3}")
result33 = my_str[::-1]
print(f"取反结果：{result33}")


# test 切片案例
str1 = '万过薪月，员序程马黑来，nohtyp学'
str2 = str1[::-1]
print(str2)  # 学python，来黑马程序员，月薪过万
list1 = str2.split('，')
str3 = list1[1]
str4 = str3.replace('来', '')
print(f"结果是：{str4}")
