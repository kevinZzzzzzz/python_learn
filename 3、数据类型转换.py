# 将数字类型转换为字符串
num_str = str(123)
print(num_str, type(num_str))

float_str = str(11.11)
print(float_str, type(float_str))
# 将字符串转换数字
num = int('123')
print(type(num), num)
num2 = float('1.11')
print(type(num2), num2)
# 错误事例  非数字字符串不能转数字
# num3 = int('哈哈哈')
# print(type(num3), num3)

# 整数转浮点数
float_num = float(12)
print(type(float_num), float_num)

# 浮点数转整数  精度丢失
num_float = int(1.9)
print(type(num_float), num_float)
