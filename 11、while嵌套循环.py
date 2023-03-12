# 外层循环的控制变量
i = 1
while i <= 100:
    print(f"今天是第{i}天，准备表白")
    # 内层循环的控制变量
    j = 1
    while j <= 10:
        print(f"送给小美的第{j}朵玫瑰花")
        j += 1
    i += 1
    print('小美我喜欢你')
print(f"坚持到第{i - 1}天，表白成功")

"""
print不换行 在后面加上end='' 
print('xxx', end='')

制表符\t  表示多行对齐
"""
print("Hello\tWorld")
print("kevin\tbest")

# test 输出九九乘法表
h = 1
while h < 10:
    n = 1
    while n <= h:
        print(f"{h} * {n} = {h * n}\t", end='')
        n += 1
    h += 1
    print()  # 换行

h2 = 9
# test 反向九九乘法表
while h2 > 0:
    n2 = 1
    while n2 <= h2:
        print(f"{h2} * {n2} = {h2 * n2}\t", end='')
        n2 += 1
    h2 -= 1
    print()