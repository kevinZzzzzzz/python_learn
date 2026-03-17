class Person:
    def __init__(self, name, age, idcard):
        self.name = name
        self._age = age
        self.__idcard = idcard

    # 注册age属性getter方法，当访问Person实例的age属性时，下面的age方法就会被自动调用
    @property
    def age(self):
        return self._age

    # 注册age属性的setter方法，当修改Person实例的age属性时，下面的age方法就会被自动修改
    @age.setter
    def age(self, value):
        self._age = value


p1 = Person('张三', 18, '1231231241231')
print(p1.name)
print(p1.age)

p1.age = 99
print(p1.age)

