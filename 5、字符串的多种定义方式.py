"""
演示字符串的三种定义方式
- 单引号
- 双引号
- 三引号
"""

name = '哈哈哈'
print(type(name), name)
name2 = "哈哈哈2"
print(type(name2), name2)
name3 = """
    111,
    222,
    333
"""
print(type(name3), name3)

# 使用 \ 转义字符 解除引号的效用
name = "haha\'2e2\"234"
print(type(name), name)

# 字符串拼接
name4 = 'kevin' + 'zzzzzz' + '123'
# 字符串无法和数字和浮点数用'+'拼接
print(name4)

