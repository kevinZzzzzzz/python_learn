"""
python 中的with主要用于管理程序中"需要成对出现的操作"，例如
    上锁/解锁
    打开/关闭
    借用/归还
最终目标：编码者只管作具体的事，进入和离开，让python自动处理
语法格式
    with 上下文管理器的表达式 as 变量:
        具体的事1
        具体的事2
        具体的事3
上下文管理器协议
    __enter__方法：with中的代码执行【之前】调用，其返回值会赋值给as后的变量
    __exit__方法：with中的代码执行【结束后】调用，无论with中是否会出现异常都会调用
        exc_type 异常类型
        exc_val  异常对象
        exc_tb   异常追踪信息
        方法返回规则如下：
            返回True：表示异常已经被处理，异常不会被继续抛出
            返回False：表示异常没有被处理，异常会被继续抛出
"""


# 定义一个Person类，让其实例对象遵循 上下文管理器协议
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'我叫{self.name},年龄是{self.age}')

    def __enter__  (self):
        print('----我是进入的逻辑------')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('----我是离开的逻辑------')
        if exc_type:
            print(exc_type)
            print(exc_val)
            print(exc_tb)
        return True

with Person('张三', 19) as p1:
    p1.speak()
    p1.study()
