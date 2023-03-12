class Student:
    # age = None
    # addr = None
    # name = None

    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr
        print(f'{self.name}信息录入完成！！！')


f = open('学生信息.txt', 'a', encoding='UTF-8')
for i in range(1, 3):
    name_s = str(input(f'请输入学生姓名：'))
    age_s = int(input(f'请输入学生年龄：'))
    addr_s = str(input(f'请输入学生地址：'))
    stu = Student(name_s, age_s, addr_s)
    f.write(f"【学生姓名：{stu.name}, 年龄：{stu.age}, 地址：{stu.addr}】")

print(f'信息录入完成！！！')
f.close()
