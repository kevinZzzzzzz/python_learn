from datetime import datetime
class Person:
    max_age = 120
    planet = '地球'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 实例方法
    def speak(self, msg):
        print(f'我叫{self.name}，年龄是{self.age}，性别是{self.gender}，我想说：{msg}')

    def run(self, distance):
        print(f'{self.name}疯狂的奔跑了{distance}米')

    """
        使用@classmethod 装饰，称作类方法
        类方法收到的参数：当前类本身（cls）自定义的参数
        因为收到cls参数，所有类方法中可以访问类属性
        类方法通常用于实现：与类相关的逻辑，例如操作类级别的信息，一些工厂方法  
    """

    @classmethod
    def change_planet(cls, value):
        cls.planet = value

    @classmethod
    def create(cls, info_str):
        name, year, gender = info_str.split('-')
        current_year = datetime.now().year
        age = current_year - int(year)
        # 创建并返回一个实例
        return cls(name, age, gender)


# 验证一下，类方法保存在类身上的
print(Person.__dict__)

# 类方法需要通过类调用
Person.change_planet('月球')
print(Person.__dict__)

p1 = Person('xx', 12, '女')
p2 = Person('xx1', 14, '女')
print(p1.planet)


p3 = Person.create('梨花-2002-女')
print(p3.__dict__)


