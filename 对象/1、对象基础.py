"""
类的定义
class 类名称:
    类的属性：定义在类中的变量
        xxx = ...
    类的行为：定义在类中的函数、方法
        def xxx(self, 形参1,...,形参N):
            ...
创建类对象的语法
    对象=类名称()

类和对象
    基于类创建对象的语法：对象名 = 类名称()
    描述：类只是一种程序内的"设计图纸"，需要基于图纸生产实体(对象)，才能正常工作，即面向对象编程
"""


class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

    def say_hi(self, msg):
        print(f'Hi大家好，我是{self.name}, {msg}')


# 创建一个对象
stu_1 = Student()
# 对象属性进行赋值
stu_1.name = 'kevinZzzzz'
stu_1.gender = '男'
stu_1.nationality = '中国'
stu_1.native_place = '广东省'
stu_1.age = 30

print(stu_1, type(stu_1))
# 获取对象中记录的信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)
stu_1.say_hi('很高兴认识大家')

stu_2 = Student()
stu_2.name = 'zzzzzkevin'
stu_2.say_hi('xixixixix')

"""
通过实例.__dict__ 可以查看实例身上的多有属性
"""
print(stu_1)  # <__main__.Student object at 0x10dde7fd0>
print(stu_1.__dict__)

"""
通过type函数，可以查看某个实例对象，是由哪个类创建出来的
"""
print(type(stu_1))  # <class '__main__.Student'>
