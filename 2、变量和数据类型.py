# 定义一个变量，用来记录钱包的余额
money = 50
# 打印 输出变量
print('钱包还有：', money)

# 买了冰淇淋，花费10元
money = money - 10

print('买了冰淇淋，花费10元，还剩余：', money)
# 买了可乐，花费5元
money = money - 5

print('买了可乐，花费5元，还剩余：', money)

# type() 语句使用方式
dict_type = type({
    'name': 123
})
print(dict_type)
string_type = type('哈哈哈哈')
print(string_type)
print(type(money))
print(type(1111))
print(type(11.11))