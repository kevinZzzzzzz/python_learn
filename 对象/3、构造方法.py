"""
构造方法
    类似于js内的construct()
    python类可以使用：__init__()方法，即构造方法
    在创建类对象（构造类）的时候，会自动执行
    在创建类对象（构造类）的时候，将传入参数自动传递给__init__方法使用
"""
class Student:
    # 可以不写，直接在__init__内定义
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建类一个对象")

stu_1 = Student('kevinZzzz', 30, '123213123123')
print(stu_1)