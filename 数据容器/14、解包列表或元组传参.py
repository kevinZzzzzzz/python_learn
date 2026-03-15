# 定义函数时名，使用*args，将收到的多个参数变成元组
def tes1(*args):
    print(f'我收到的参数是，{args}, 参数类型：{type(args)}')

list1 = [1,2,3,4,5]
tuple1 = (1, '23', 'hahah')
# 函数调用时，使用*对 列表 或者 元组 进行解包后，再传递参数
# 调用函数时，用*解包
tes1(*list1)
tes1(*tuple1)
"""
我收到的参数是，(1, 2, 3, 4, 5), 参数类型：<class 'tuple'>
我收到的参数是，(1, '23', 'hahah'), 参数类型：<class 'tuple'>
"""
