num1 = int(input('输入班级1的学生数量'))
class1 = set()

for i in range(0, num1):
    name = input('输入的学生%d姓名:' % (i + 1))
    class1.add(name)

print(class1)
