# 算数运算符
print("1 + 1 =", 1 + 1)
# print(1 + 'haha')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print("2 - 1 =", 2 - 1)
print("2 * 1 =", 2 * 1)
print("4 / 2 =", 4 / 2)
# 取整除
print("10 // 3 =", 10 // 3)
# 取余
print("10 % 3 =", 10 % 3)
# 指数
print("2 ** 2 =", 2 ** 2)

# 复合赋值
num = 10
num += 1
print("num += 1", num)
num -= 1
print("num -= 1", num)
num *= 2
print("num *= 2", num)
num /= 2
print("num /= 2", num)
num %= 3  # 取余
print("num %= 3", num)
num = 4
num **= 2  # 指数
print("num **= 2", num)
num //= 1  # 取整
print("num //= 1", num)
