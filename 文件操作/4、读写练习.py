
r = open('./bill.txt', 'r', encoding='UTF-8')
w = open('./bill.txt.bak', 'w', encoding="UTF-8")

for i in r.readlines()[0::]:
    temp = i
    if temp.strip().split(',')[-1] == '测试':
        continue
    w.write(i)
r.close()
w.close()
