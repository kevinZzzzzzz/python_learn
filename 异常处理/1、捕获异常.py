"""
基本语法：
    try：
        xxx
    except：
        xxx
"""
# 尝试打开读取某个文件，如果文件不存在，就新建一个文件打开
try:
    f = open('linux.txt', 'r')
except:
    w = open('linux.txt', 'w')
    w.write('hello world')
    w.close()
finally:
    f.close()
# 捕获指定异常
try:
    # print(name)  # NameError
    1 / 0   # ZeroDivisionError
except (NameError, ZeroDivisionError) as e:
    print(e)
    print('出现变量为定义异常')

# 捕获所有异常
try:
    # name = 123
    print(name)  # NameError
    # 1 / 0   # ZeroDivisionError
except Exception as e:
    print('出现变量为定义异常')
else:
    print('没有异常，才会执行')
finally:    # 无论如何都会执行
    print('不管有没有异常，一定执行')
