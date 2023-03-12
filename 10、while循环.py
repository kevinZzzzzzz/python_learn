"""
while循环
while 条件：
    条件满足时，做的事情1
    条件满足时，做的事情2
    条件满足时，做的事情3
    。。。
"""
# count = int(0)
# while count < 100:
#     print("哈哈哈", count)
#     count += 1

# test 计算1 到 100 的和
num = int(1)
num2 = int(0)
while num <= 100:
    num2 += num
    num += 1
print(f"1到100累计：{num2}")

# test 设置1-100随机整数，判断输入的数字是否等于随机数
import random
count2 = random.randint(1, 100)
num4 = int(0)  # 猜测的次数
flag = True
while flag:
    num3 = int(input('您输入的数字：'))
    num4 += 1
    if num3 == count2:
        print(f'恭喜你猜对了,一共猜了{num4}次')
        flag = False
    else:
        if num3 > count2:
            print('大了')
        else:
            print('小了')
