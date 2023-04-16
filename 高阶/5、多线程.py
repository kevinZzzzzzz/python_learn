"""
多线程
    threading模块实现python的多线程
    thread_obj = threading.Thread([group [, target [, name [, agrs [.kwargs]]])
        group: 暂时无用，未来功能的预留参数
        target: 执行的目标任务名
        args：以元组的方式给执行任务传参
        kwargs：以字典的方式给执行任务传参
        name：线程名，一般不用设置
#    启动线程，让线程开始工作
        thread_obj.start()
"""
import threading
import time


def sing(msg):
    while True:
        print('我在唱歌，啦啦啦。。。' + msg)
        time.sleep(1)

def dance(msg):
    while True:
        print('我在跳舞，瓜瓜瓜。。。' + msg)
        time.sleep(1)

# 单线程下 sing函数会一直执行， dance不会执行
# sing()
# dance()
sing_fun = threading.Thread(target=sing, args=('哈哈哈哈',))
dance_fun = threading.Thread(target=dance, kwargs={'msg': 'hahaha'})

sing_fun.start()
dance_fun.start()