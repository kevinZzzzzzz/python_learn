"""
装饰器
1、装饰器是一种【可调用对象】(通常是函数)，它能够接收一个函数作为参数，并且会返回一个新函数
2、装饰器可以在不修改原函数代码的前提下，增强或改变原函数的功能
"""

# def add(x, y):
#     res = x + y
#     print(f'{x}和{y}相加的结果是：{res}')
#     return res
#
# result = add(10, 20)
# print(result)
#
#
# def say_hello(fn):
#     def wrapper(*args, **kwargs ):
#         print('hello')
#         res = fn(*args, **kwargs)
#         return res
#     return wrapper
# # 需求，在不修改add 函数的前提下，给add函数增加一些额外的功能，例如：计算前先打印一句欢迎语
# add_pro = say_hello(add)
# result2 = add_pro(10, 20)
# print(result2)


def say_hello(fn):
    def wrapper(*args, **kwargs ):
        print('hello')
        res = fn(*args, **kwargs)
        return res
    return wrapper

@say_hello
def add(x, y):
    res = x + y
    print(f'{x}和{y}相加的结果是：{res}')
    return res

res1 = add(10, 20)
print(res1)
