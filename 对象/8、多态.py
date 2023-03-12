"""
多态：在完成某个行为时，使用不同的对象会得到不同的状态
"""
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print('汪汪汪')

class Cat(Animal):
    def speak(self):
        print('喵喵喵')

def make_noise(animal: Animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)

"""
抽象类：
    好比定义好一个标准,包含了一些抽象的方法，要求子类必须实现
"""
class AC:
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_l_r(self):
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print('美的空调核心制冷科技')
    def hot_wind(self):
        print('美的空调电热丝加热')
    def swing_l_r(self):
        print('美的空调无风感左右摆风')

class GREE_AC(AC):
    def cool_wind(self):
        print('格力空调变频省电制冷')
    def hot_wind(self):
        print('格力空调电热丝加热')
    def swing_l_r(self):
        print('格力空调静音左右摆风')

