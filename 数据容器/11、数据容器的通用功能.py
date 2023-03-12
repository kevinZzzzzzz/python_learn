my_list = [1, 2, 3, 4, 5, 6]
my_tuple = (1, 2, 3, 4, 5, 6)
my_str = 'abcdefg'
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4}

print(len(my_list))
print(len(my_tuple))
print(len(my_str))
print(len(my_set))
print(len(my_dict))

print(max(my_list))
print(max(my_tuple))
print(max(my_str))
print(max(my_set))
print(max(my_dict))

print(min(my_list))
print(min(my_tuple))
print(min(my_str))
print(min(my_set))
print(min(my_dict))

"""
容器类型转换
list()、tuple()、str()、set()、dict()
"""
print('转列表===========')
print(f'列表->列表', list(my_list))
print(f'元组->列表', list(my_tuple))
print(f'字符串->列表', list(my_str))
print(f'集合->列表', list(my_set))
print(f'字典->列表', list(my_dict))
print('转元组===========')
print(f'列表->元组', tuple(my_list))
print(f'元组->元组', tuple(my_tuple))
print(f'字符串->元组', tuple(my_str))
print(f'集合->元组', tuple(my_set))
print(f'字典->元组', tuple(my_dict))
print('转字符串===========')
print(f'列表->字符串', str(my_list), type(str(my_list)))
print(f'元组->字符串', str(my_tuple), type(str(my_tuple)))
print(f'字符串->字符串', str(my_str), type(str(my_str)))
print(f'集合->字符串', str(my_set), type(str(my_set)))
print(f'字典->字符串', str(my_dict), type(str(my_dict)))
print('转集合===========')
print(f'列表->集合', set(my_list), type(set(my_list)))
print(f'元组->集合', set(my_tuple), type(set(my_tuple)))
print(f'字符串->集合', set(my_str), type(set(my_str)))
print(f'集合->集合', set(my_set), type(set(my_set)))

# 其他容器类型 无法转换程字典！！！！
# print('转字典===========')
# print(f'列表->字典', dict(my_list), type(dict(my_list)))
# print(f'元组->字典', dict(my_tuple), type(dict(my_tuple)))
# print(f'字符串->字典', dict(my_str), type(dict(my_str)))
# print(f'集合->字典', dict(my_set), type(dict(my_set)))
# print(f'字典->字典', dict(my_dict), type(dict(my_dict)))

"""
容器通用排序功能
    sorted(容器, [reverse=True])
    reverse: 反向
    结果都会变成列表对象
"""
my_list1 = [4, 2, 5, 6, 3, 9, 7, 8]
my_tuple1 = (4, 2, 5, 6, 3, 9, 7, 8)
my_str1 = 'asdfghjkl'
my_set1 = {4, 2, 5, 6, 3, 9, 7, 8}
my_dict1 = {"key": 3, "3key2": 2, "key3": 8, "key4": 6}
print(sorted(my_list1))
print(sorted(my_tuple1))
print(sorted(my_str1))
print(sorted(my_set1))
print(sorted(my_dict1))
print(sorted(my_list1, reverse=False))
print(sorted(my_tuple1, reverse=False))
print(sorted(my_str1, reverse=False))
print(sorted(my_set1, reverse=False))
print(sorted(my_dict1, reverse=False))
