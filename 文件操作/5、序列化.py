"""
默认情况下，只能将字符串写入文件中
对象是无法写入文件中，必须先作序列化操作
"""
fp = open('text.txt', 'w')
name_list = [1, 2, 3, 4]
# fp.write(name_list) # 应为类型 'str' (匹配的泛型类型 'AnyStr')，但实际为 'list[int]'
# 序列化的两种方式
import json
context = json.dumps(name_list)  # 将对象变成json字符串
print(type(context)) # <class 'str'>
fp.write(context)
fp.close()


# dump  在将对象转换为字符串的同时，指定一个文件的对象，然后吧转换后的字符串写入到这个文件中
fp = open('text1.txt', 'w')
name_list = [1, 2, 3, 4]
import json
json.dump(name_list, fp)
fp.close()