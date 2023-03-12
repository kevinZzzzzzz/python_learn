"""
for 临时变量 in 序列类型数集
    。。。
序列类型:字符串、列表、元祖。。。

语法一:
    range(num) ===> 类似js里面new Array(num)
    range(5) ===> [0,1,2,3,4]
语法二:
    range(num1, num2)表示从num1开始到num2结束
    range(5, 10) ===> [5,6,7,8,9]
语法三:
    range(num1, num2, step): step表示间距，默认1
    range(5,10,2) ===> [5,7,9]
"""
for x in range(10):
    print(f'{x}、', end='')
print()
for x in range(5, 10):
    print(f'{x}、', end='')
print()
for x in range(5, 10, 2):
    print(f'{x}、', end='')
print()

"""
for 循环的变量作用域
在for循环外部访问临时变量
实际是可以访问到的,但在编程规范上是不允许的
"""
x = 0
for x in range(5):
    print(x)
print(x)  # ❌不建议
