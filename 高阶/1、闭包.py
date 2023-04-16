"""
闭包
    在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数，我们就把这个使用的外部函数变量的内部函数称为 闭包
    内部函数修改外部函数的变量
        使用nonlocal关键字修饰该变量
    优点：
        无需定义全部变量即可实现通过函数持续的访问、修改某个值
        闭包使用的变量的所用于在函数内，难以被错误的调用修改
    缺点：
        由于内部函数持续引用外部函数的值，所有会导致这一部分的内存空间不被释放，一直占用内存
"""
# 简单闭包
def outer(logo):
    def inner(msg):  # 内部函数inner使用外部函数outer的logo变量
        print(f"<{logo}> - {msg} - <{logo}>")
    return inner

fn1 = outer('哈哈哈哈')
fn1('kevinZzzzz')

fn2 = outer('ehehheehe')
fn2('kevinZzzzzz')

# 使用nonlocal关键字修改外部函数的值
def outer1(num1):
    def inner(num2):
        nonlocal num1
        num1 += num2
        print(num1)
    return inner

fn = outer1(10)
fn(10)
fn(10)

# 使用闭包实现ATM个例
def account_create(initial_amount=0):
    def atm(num, deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存款， {num}, 账户余额：{initial_amount}")
        else:
            initial_amount -= num
            print(f"取款， {num}, 账户余额：{initial_amount}")
    return atm

atm1 = account_create(1000)
atm1(100)
atm1(100)
atm1(200, False)
