import os
'''
练习：将二进制文件复制到指定位置
'''

# 源文件
source = 'b.png'
# 目标位置
target = 'dome/aa/bb/cc'
# target = 'dome/aa/bb/cc/ddr'

# 判断目录是否存在, 如果不存在则创建
if not os.path.isdir(target):
    os.makedirs(target)
# with open(source, 'rb') as f1, open(target + '/' + 'bb.png', 'wb') as f2:
#     data = f1.read()
#     f2.write(data)
with open(source, 'rb') as f1, open(target + '/' + 'bb.png', 'wb') as f2:
    while True:
        # 每次只读1kb
        data = f1.read(1024)
        if not data:
            break
        f2.write(data)