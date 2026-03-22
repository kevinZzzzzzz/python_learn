a = 666
print(id(a))
print(hex(id(a)))
b = a
print(id(b), id(a))

"""
python 不可变对象： int, float, bool, str, tuple, frozenset, None
可变对象：list, dict, set, 自定义类的实例对象
"""