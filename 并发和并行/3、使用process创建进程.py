import os
import time
from multiprocessing import Process


# 定义一个speak函数，功能是：，每隔一秒说话一次（一共说10次）
def speak():
    for index in range(10):
        print(f'我在说话{index}，进程pid是：{os.getppid()}, 父进程pid是：{os.getppid()}')
        time.sleep(1)


# 定义一个study函数，功能是：每隔一秒学习一次（一共学习15次）
def study():
    for index in range(15):
        print(f'我在学习{index}，进程pid是：{os.getppid()}, 父进程pid是：{os.getppid()}')
        time.sleep(1)
  

# 先学习在说话
# speak()
# study()

'''
注意一定要写if __name__ == '__main__'，这个判断，原因如下
    当创建子进程时，Python并不会把父进程内存里的speak函数直接交给子进程
    python会启动一个全新的python 解释器进程，重新执行当前的。py文件（作为模块）
    在执行过程中，重新定一个speak函数，交给子进程
'''
if __name__ == '__main__':
    # 创建两个Process 类的实例对象（进程对象），分别是p1 和 p2
    # 注意点1：p1 和 p2就对应着以后的两个子进程，在创建它们的说话，就要指定好他们要执行的任务
    # 注意点2：此时的p1和p2 只是代码层面的两个进程对象，操作系统还没有真的创建p1 和 p2两个进程

    p1 = Process(target=speak)
    p2 = Process(target=study)
    # 调用进程对象的start方法，会立刻向操作系统申请一个进程，并且会将该进程交由操作系统进行调度
    p1.start()
    p2.start()
