file = open(file='a.txt', mode='r', encoding='utf-8')
# result = file.read()

# 多次调用
# r1 = file.read(2)
# r2 = file.read(3)
# r3 = file.read(5)
# r4 = file.read()
# print(r1)
# print(r2)
# print(repr(r3))   # '\n黄河入海'
# print(r4)
# file.close()

# 用循环调用read（对内存友好）
while True:
    result = file.read(10)
    if result == '':
        break
    print(result, end='')
file.close()

file2 = open('b.png', 'rb')
result2 = file2.read()
# print(result2)
file2.close()
