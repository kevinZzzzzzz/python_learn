"""
文件操作步骤
1、打开文件
    open(name,mode,encoding)
        name:要打开的目标文件名的字符串或者所在路径
        mode:设置打开文件的访问模式：只读r、写入w、追加a等
        encoding: 编码格式UTF-8
2、读写文件
    file.read()  file.wirte()
3、关闭文件
    file.close()
"""
from datetime import time

# 打开文件
f = open('python.txt', 'r', encoding='UTF-8')
print(type(f))  # <class '_io.TextIOWrapper'>
# 读取文件 - read()
print(f"读取10个字节的结果：{f.read(10)}")
print(f"读取全部内容的结果：{f.read()}")
# 读取文件的全部行 readLines()
f = open('python.txt', 'r', encoding='UTF-8')
line = f.readlines()
print(f"lines对象的类型:{type(line)}")  # <class 'list'>
print(f"line对象的内容:{line}")
# 读取单行 readLine()
f = open('python.txt', 'r', encoding='UTF-8')
line = f.readline()
print(f"lines对象的类型:{type(line)}")  # <class 'str'>
print(f"line对象第1行的内容:{line}")  # 哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈1
line = f.readline()
print(f"line对象第2行的内容:{line}")  # 哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈2
line = f.readline()
print(f"line对象第3行的内容:{line}")  # 哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈3
# 遍历文件对象
f = open('python.txt', 'r', encoding="UTF-8")
for i in f:
    print(i)

# 文件的关闭
f.close()

# with open语法  向比较于open方法，with open方法调用完后会自动调用f.close()
with open('python.txt', 'r') as f:
    for i in f:
        print(f'每一行的数据是：{i}')


# 计算python.txt文件内"呵"的数量
count1 = 0
with open('python.txt', 'r') as f:
    for i in f:
        print(i)
        count1 += i.count('呵呵')
print(f"呵出现的次数有：{count1}")


