"""
文件操作步骤
1、打开文件
    open(name,mode,encoding,error=None)
        name:要打开的目标文件名的字符串或者所在路径
        mode:设置打开文件的访问模式：只读r、写入w、追加a等
            t：以文本文件模式打开文件
            b：以二进制文件模式打开文件
            r：以只读模式打开文件
            w：以只写模式打开文件，不能读内容，如果文件不存在会创建文件；如果存在，会覆盖原来的内容
            x：以独占创建模式打开文件，如果文件不存在，则创建并以写入模式打开，如果文件存在，会引发FIleExistsError异常
            a：以追加模式打开文件，不能读内容。如果文件不存在，则创建文件；如果文件存在，则在文件末尾追加内容
            +：以更新（读写）模式打开文件，必须与r、w或者a组合使用，才能设置文件为读写模式
        encoding: 编码格式UTF-8
        error参数：用来指定在文本文件发生编码错误时如何处理。
                ignore 表示遇到编码错误时忽略该错误，程序会继续进行，不会退出
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


