from datetime import datetime

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 静态方法
    # 使用 @staticmethod 装饰过的方法，就叫静态方法，静态方法也是保存在类身上的
    # 静态方法只是单纯的定义在类中，不会收到self，cls 参数, 收到的参数都是自定义参数
    # 由于静态方法没有收到self、cls参数，所以其内部不会访问任何类和实例相关的内容
    # 静态方法通常用于定义：与类相关的工具方法
    @staticmethod
    def is_adult(year):
        # 获取当前年份
        curr_year = datetime.now().year
        age = curr_year - year
        return age >= 18

# 静态方法需要通过类去调用
result = Person.is_adult(1972)
print(result)

