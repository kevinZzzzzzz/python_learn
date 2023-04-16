"""
装饰器
    其实也是一种闭包，其功能就是在不破坏目标函数原油的代码和功能的前提下，为目标函数增加新的功能
"""

# def sleep():
#     import random
#     import time
#     print('睡眠中。。。。')
#     time.sleep(random.randint(1, 5))
# print('我要睡觉了')
# sleep()
# print('我醒了')
def outer(fun):
    def inner():
        print('我要睡觉了')
        fun()
        print('我醒了')
    return inner

# def sleep():
#     import random
#     import time
#     print('睡眠中。。。。')
#     time.sleep(random.randint(1, 5))
#
# fn = outer(sleep)
# fn()

@outer
def sleep():
    import random
    import time
    print('睡眠中。。。。')
    time.sleep(random.randint(1, 5))
sleep()