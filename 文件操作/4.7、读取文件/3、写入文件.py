import time

with open('b.txt', 'wt', encoding='utf-8') as file:
    file.write('hello')

# x 如果文件不存在，则创建并以写入模式打开，如果文件存在，会引发FIleExistsError异常
# with open('demo.txt', 'xt', encoding='utf-8') as file:
#     file.write('你好啊')


# python写入文件，并不是每次写一次就立刻落盘，而是先写入到'缓冲区'里
# 然后用flush方法从缓冲区里面拿出来,立刻写入到文件中
# with open('a.txt', 'at', encoding='utf-8') as file:
#     file.write('\n你好1')
#     file.write('\n你好2')
#     file.flush()
#     time.sleep(1000)
#     file.write('\n你好3')
#     file.write('\n你好4')

# 测试rt+
with open('a.txt', 'rt+', encoding='utf-8') as file:
    """
        seek(offset, whence)方法：用于改变文件对象指针的位置，参考说明如下
            offset: 偏移量，要移动多少距离
            whence：参考点， 从哪里开始计算偏移，有三种取值
                0-从文件开头计算（默认值）
                1-当前位置
                2-文件末尾
        注意：文本模式下，不要随意去定位中文字符位置，否则可能破坏文件编码
    """
    file.seek(0, 0)
    file.write('你好xxxxx')
