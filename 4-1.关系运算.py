a = int(input("输入我们球队的实力:"))
b = int(input('输入对手1的实力:'))
c = int(input('输入对手2的实力:'))
d = int(input('输入对手3的实力:'))

print(+(a == b))
avsb = (a > b) * 3 + (a == b)
avsc = (a > c) * 3 + (a == c)
cvsb = (c > b) * 3 + (c == b)

scope = avsb + avsc + cvsb

print("小组赛球队得%d分。"%(scope))