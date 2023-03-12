"""
大数据、Spark Flink
"""
# 函数作为参数
def test_func(fn):
    print(type(fn))  # <class 'function'>
    result = fn(1, 2)
    print(result)

def compute(x, y):
    return x + y

test_func(compute)

"""
匿名函数语法
lambda 传入参数: 函数体（一行代码）
·lambda是关键字，表示定义匿名函数
·传入参数表示匿名函数的形式参数，如x, y表示接收2个形式参数
·函数体，就是函数的执行逻辑，要注意只能写一行，无法多行
"""
def test_func(fn):
    result = fn(2, 2)
    print(result)

test_func(lambda x, y: x + y)
