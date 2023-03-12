"""
    循环中断
    continue 和 break
    continue：中断单次次循环，直接进入下一次循环
    break：跳出循环
"""
# continue
for i in range(1, 5):
    print(1)
    continue
    print(2)
# continue嵌套应用
for i in range(1, 6):
    print(1)
    for j in range(1, 6):
        print(2)
        continue
        print(3)
print(4)

# break
i = 0
while i <= 10:
    i += 1
    print(i)
    break
print(i)


# break 嵌套应用
for i in range(1, 6):
    print('语句1')
    for j in range(1, 6):
        print("语句2")
        break
        print("语句3")
    print("语句4")
