
num = 10  # 定义一个全局变量
def test_a():
    num = 100  # 局部变量
    print(num)

test_a()
print(num)

# global 关键字  可以将函数内部声明的变量为全局变量
num1 = 10  # 定义一个全局变量
def test_a():
    global num1  # 定义一个全局变量
    num1 = 100  # 局部变量
    print(num1)

test_a()
print(num1)
