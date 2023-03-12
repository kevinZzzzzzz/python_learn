
# 构建一个随机数, 三次猜测
import random
num = random.randint(1, 10)
guess_num = int(input('请输入数字:'))
if guess_num == num:
    print('yes first')
else:
    if guess_num > num:
        print('bigger')
    else:
        print('less')
    guess_num = int(input('请输入数字:'))
    if guess_num == num:
        print('yes second')
    else:
        if guess_num > num:
            print('bigger')
        else:
            print('less')
        guess_num = int(input('请输入数字:'))
        if guess_num == num:
            print('yes third')
        else:
            print('三次机会用完了')
