"""
通过'键=值'形式传递参数，可以不限制参数顺序
可以和参数混用，位置参数需在前
"""


def user_info(name, age, gender):
    print(f"您的姓名是：{name},年龄是：{age},性别是：{gender}")


# 关键字传参
user_info(name='kevinZzzzzz', age=23, gender='男')
# 可以不按固定顺序
user_info(age=20, gender="男", name="kevinzzzzzz")
# 可以和位置参数混用，位置参数必须在前，且匹配参数顺序
user_info("小明", age=20, gender='男')


# 默认值  必须设置在最后
def user_info1(name, age=11, gender='男'):
    print(f"您的姓名是：{name},年龄是：{age},性别是：{gender}")


user_info1('哈哈', 29)


# 不定长 - 位置不定场，*号 -> *args
# 不定长定义的形式参数会作为 元组 存在，接受不定长数量的参数传入
def user_info2(*args):
    print(f'args参数的类型是：{type(args)}，内容是：{args}')

user_info2(1, 2, 3, '小明', '男')

# 不定长 - 关键字不定长， **号 -> **kwargs
# 不定长定义的形式参数会作为 字典 存在，接受不定长数量的参数传入
def user_info3(**kwargs):
    print(f'kwargs参数的类型是：{type(kwargs)}，内容是：{kwargs}')
user_info3(name='kevin', age="11", gender='男', addr='北京')
