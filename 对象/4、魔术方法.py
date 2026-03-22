"""
魔术方法：即python内置方法，
__init__构造方法，用于创建类对象的时候设置初始化行为
__str__字符串方法  得到内存地址
    直接比较两个对象是不可以的,需要重新定义
__lt__小于符号比较方法 <
    用于对象1的某个属性和对象2的某个属性的比较
    传入参数：另一个对象的某个属性
    返回值：True或者False
__gt__大于符号比较方法 >
__le__小于等于符号比较方法 >=
__ge__大于等于符号比较方法 >=
__eq__相等符号比较方法 ==
"""
class Student:
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建类一个对象")

stu_1 = Student('kevinZzzz', 31, '123213123123')
stu_2 =  Student('哈哈哈哈', 31, '43235235234')

# __str__
print(stu_1.__str__())  # <__main__.Student object at 0x10ac150d0>
print(stu_1.__lt__(stu_2))  # NotImplemented 直接比较两个对象是不可以的,需要重新定义
print(stu_1.age.__lt__(stu_2.age)) #  等同于print(stu_1.age < stu_2.age)
print(stu_1.age < stu_2.age)
print(stu_1.age.__gt__(stu_2.age)) #  等同于print(stu_1.age > stu_2.age)
print(stu_1.age > stu_2.age)
print(stu_1.age.__le__(stu_2.age)) #  等同于print(stu_1.age > stu_2.age)
print(stu_1.age >= stu_2.age)
print(stu_1.age.__eq__(stu_2.age))
print(stu_1.age == stu_2.age)