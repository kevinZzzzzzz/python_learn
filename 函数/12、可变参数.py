"""
函数-可变参数
    定义函数时，在形参名前加*，可以接收任意数量的 位置参数，并打包成一个元组
    定义函数时，在形参名前加**, 可以接收任意数量的 关键字参数，并打包成一个字典
"""


def thaaa1(*args):
    print(args, type(args))


thaaa1('213', 321, True)

def thaaa2(**kwargs):
    print(kwargs, type(kwargs))

thaaa2(a='213', b=321, c=True)


def thaaa3(*args, **kwargs):
    print(args, kwargs)

thaaa3('213', 321, True, a='213', b=321, c=True)
