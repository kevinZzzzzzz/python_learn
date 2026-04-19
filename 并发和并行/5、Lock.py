import os
import time
from multiprocessing import Process, Manager, current_process


def speak(lock):
    for index in range(10):
        # 上锁：如果锁是空闲的，立刻上锁，继续往下执行，如果锁被别人拿着，当前进程会阻塞等待（原地等）
        lock.acquire()
        print(f'{current_process().name}-----我在说话{index}，进程pid是：{os.getpid()}, 父进程pid是：{os.getppid()}')
        print('A', end='')
        print('B', end='')
        print('C', end='')
        print('D')
        # 释放锁：acquire 和 release 必须成对出现，否则会永远卡住，死等
        lock.release()
        time.sleep(1)


def study(lock):
    for index in range(15):
        with lock:
            # 会自动执行acquire和release，即便报错也会释放锁
            print(f'我在学习{index}，进程pid是：{os.getpid()}, 父进程pid是：{os.getppid()}')
        time.sleep(1)


if __name__ == '__main__':
    # 🔥 关键修复：用 Manager 创建可传递的锁
    with Manager() as manager:
        # lock = manager.Lock()  # 代替原来的 Lock()
        lock = manager.RLock()  # 处理多个锁问题

        p1 = Process(target=speak, name='说话进程', args=(lock,))
        p2 = Process(target=study, args=(lock,))
        p1.start()
        p2.start()

        p1.join()
        p2.join()

# 出现插队的问题
'''
...... 
哈哈啊哈，我在学习4，进程pid是：53676, 父进程pid是：53676
100-200说话进程-----我在说话4，进程pid是：53676, 父进程pid是：53676
哈哈啊哈，我在学习5，进程pid是：53676, 父进程pid是：53676100-200说话进程-----我在说话5，进程pid是：53676, 父进程pid是：53676

哈哈啊哈，我在学习6，进程pid是：53676, 父进程pid是：53676
100-200说话进程-----我在说话6，进程pid是：53676, 父进程pid是：53676
哈哈啊哈，我在学习7，进程pid是：53676, 父进程pid是：53676
100-200说话进程-----我在说话7，进程pid是：53676, 父进程pid是：53676
'''