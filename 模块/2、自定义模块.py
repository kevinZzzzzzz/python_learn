import my_module
print(my_module.test(1, 2))

from my_module import test
print(test(2, 3))

from my_module import *
# print(test2(3, 2)) # 未解析的引用 'test2'
