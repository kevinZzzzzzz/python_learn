"""
写入操作
    打开文件
        f = open('xxx', 'w')
    写入文件
        # f.write(xxx)   会积攒在程序的内存中，成为缓冲区
    内容刷新
        f.flush()   内容真正写入文件
    关闭文件
        f.close()   内置flush方法
"""
f = open('python1.txt', 'w', encoding="UTF-8")
f.write('hello world!!!!')
# f.flush()
# f.close()
