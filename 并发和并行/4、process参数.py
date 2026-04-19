import os
import time
from multiprocessing import Process, current_process


def speak(a, b):
    for index in range(10):
        print(f'{a}-{b}{current_process().name}-----我在说话{index}，进程pid是：{os.getppid()}, 父进程pid是：{os.getppid()}')
        time.sleep(1)


def study(msg):
    for index in range(15):
        print(f'{msg}，我在学习{index}，进程pid是：{os.getppid()}, 父进程pid是：{os.getppid()}')
        time.sleep(1)


if __name__ == '__main__':
    '''
        Process参数
        group 默认值为None（应当始终为None）
        target 子进程要执行的可调用对象，默认值为None
        name 进程名称，默认值为None。如果设置为None，python会自动分配名称
        args 给target传的位置参数（元组）
        kwargs 给target传的关键字参数（字典）
        daemon 标记进程是否为守护进程，取值为布尔值（默认为None，表示从创建方进程继承）
    '''
    p1 = Process(target=speak, name='说话进程', args=(100, 200))
    p2 = Process(target=study, kwargs={'msg': '哈哈啊哈'})
    print(p1.name)
    print(p2.name)
    # 调用进程对象的start方法，会立刻向操作系统申请一个进程，并且会将该进程交由操作系统进行调度
    p1.start()
    p2.start()
