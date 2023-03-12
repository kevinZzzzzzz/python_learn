"""
for循环
for 临时变量 in 待处理的数集:
    。。。
"""
arr = [1, 2, 3, 4]
for i in arr:
    print(i, end='')
print()

# 计算文案中几个z
num = 0
str1 = 'kevinzzzzz'
for i in str1:
    if i == 'z':
        num += 1
print(f"str内一共有{num}个a")