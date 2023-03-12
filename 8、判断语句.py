"""
布尔类型
是:True
否: False
"""
# 比较运算符
result = 10 > 5
print(f"10 > 5 的结果是：{result}， 类型是：{type(result)}")

# if 语句
"""
if 要判断的条件:
    成立时要做的事情
else 
    不成立时要做的事情
"""
age = int(input('请输入你的年龄:'))
print('你的年龄是%d,' % age)
if age >= 18:
    print('成年了')
elif age >= 20:
    print('大学毕业了')
else:
    print('好好学习')

print(f"{age}哈哈哈哈")

# test
print('欢迎来到动物园')
cm = int(input('请输入你的身高(cm)：'))
if cm > 120:
    print(f"您的身高{cm}cm，超过120cm，游玩需要支付10元")
else:
    print(f"您的身高{cm}cm，未超过120cm，可以免费游玩")
print('祝您玩的愉快!!!!')

# if 嵌套语句:
"""
if 条件一:
    ...
    if 条件二：
        ...
    else:
        ...
else：
    ...
"""
