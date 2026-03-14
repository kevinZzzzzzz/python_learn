"""
函数限制传参方式
具体规则：/ 前边只能用位置参数，* 后面只能用关键字参数
"""

def greet(name, /, gender, *, age, height):
    print(f'我叫{name}, 性别{gender}, 年龄是{age}, 身高{height}cm')

# 正确方式
greet('张三', '男', age=18, height=180)
greet('里斯', gender='男', age=29, height=160)

# 错误方式
# TypeError: greet() got some positional-only arguments passed as keyword arguments: 'name'
# greet(name='张三', gender='男', age=18, height=180)

# TypeError: greet() takes 2 positional arguments but 3 positional arguments (and 1 keyword-only argument) were given
# greet('张三', '男', 18, height=172)
