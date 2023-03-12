
"""
__all__ = []   列表结构
如果一个模块中有__all__变量，当使用  from xxx import *   导入时，只能导入这个列表中的元素
"""
__all__ = ['test']

def test(x, y):
    return x + y

def test2(x, y):
    return x - y

# print(__name__)
if __name__ == '__main__':  # 当运行当前模块时为true  当通过模块import的方式时为false
    print(test(2, 3))
    print(test2(2, 3))
