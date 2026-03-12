"""
    元组:相较于列表大致相同，但是不能修改元素
    定义：
        字面量：(元素1，元素2，元素3。。。)
        元组变量：
            变量名称 = (元素1，元素2，元素3。。。)
        tip: 元组只有一个数据，这个数据后面必须添加逗号 t2 = ('hello',)
        定义空元组
            变量名称 = ()
            变量名称 = tuple()
"""
# 定义元组
t1 = (1, 'hello', True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：", {type(t1)}, t1, t2, t3)

t4 = ('hello')
print(t4, type(t4))  # hello <class 'str'>

t5 = ('hello',)
print(t5, type(t5))  # ('hello',) <class 'tuple'>

# 元组的嵌套
t6 = ((1, 2, 3, 4), (1, 2, 3, 4))
print(t6, type(t6))

# 下标索引取出内容
ele = t6[0][2]
print(f"t6的第一个元素的第3个元素{ele}")

# 查找元素下标
index = t1.index('hello')
print(f"hello在元组内的位置是{index}")


# 统计某个元素在元组内的数量
num = t1.count(1)
print(f"1在元组t1内出现了{num}次")

# 统计元组内的元素个数
print(len(t6))


# 元组的遍历
def tuple_while():
    index = 0
    while index < len(t1):
        ele = t1[index]
        print(f"{ele}, 12")
        index += 1

def tuple_for():
    for i in t1:
        print(i, t1.index(i))

tuple_while()
tuple_for()


# 元组的修改  非列表元素不可修改
t7 = (1, 2, 3)
# t7[0] = 2  #  'tuple' object does not support item assignment
t8 = (1, 2, [2, 3, 5])
t8[2][1] = 10
print(t8)