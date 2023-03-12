"""
    test
    坚持表白100天，每天送一朵花
"""
for i in range(1, 101):
    print(f"今天是向小美表白的第{i}天，加油坚持")
    # 内层嵌套
    for j in range(1, 11):
        print(f"给小美送的第{j}朵玫瑰花")
    print(f'小美我喜欢你')
print(f"表白成功")

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{i} * {j} = {i * j}\t", end="")
    print()

for i in range(9, 0, -1):
    for j in range(1, i+1):
        print(f"{i} * {j} = {i * j}\t", end="")
    print()

