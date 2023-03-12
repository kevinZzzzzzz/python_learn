"""
某公司，账户余额有1w元，给20位员工发工资
员工1-20，依次领取工资，每人领取1000元
随机生成绩效（1-10），如果低于5，则不发工资
如果工资发完，则结束发工资
"""

import random
count = 10000
for i in range(1, 21):
    num = random.randint(1, 10)
    if count <= 0:
        print(f"工资发完了，下个月来领取吧～")
        break
    if num < 5:
        print(f"员工{i}, 绩效分{num}, 低于5,不发奖金，下一位")
        continue
    count -= 1000
    print(f"向绩效分为{num}的员工{i}发放工资1000元，账户余额还剩{count}元")

