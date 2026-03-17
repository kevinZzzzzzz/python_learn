# 方法1：isinstance(instance, Class) 作用：判断某个对象是否为指定类或者其子类的实例
# 方法2：issubclass(Class1, Class2) 作用：判断某个类是否是另一个类的子类

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    def __init__(self, name, age, gender, stu_id, grade):
        super().__init__(name, age, gender)
        self.stu_id = stu_id
        self.grade = grade


p1 = Person('张三', 18, "男")
s1 = Student('梨花', 12, '男', '2025001', '初二')

print(isinstance(p1, Person))
print(isinstance(s1, Student))
print(isinstance(s1, Person))
print(isinstance(p1, Student))


print(issubclass(Student, Person))
