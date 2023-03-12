money = 5000000
name = str(input('请输入您的称呼：'))


def checkSum(show_header):
    if show_header:
        print('------查询余额--------')
    print(f'{name},您好，您的余额剩余: {money}元')


def addMoney(sum):
    global money, name
    money += sum
    print('----------存款----------')
    print(f'{name}, 您好,您存款{sum}成功')

    checkSum(False)


def getMoney():
    global money, name
    count = int(input('请输入您要取得的金额：'))
    if count > money:
        print('对不起，取款金额不能超过存款金额')
    else:
        money -= count
        print(f'{name}, 您好,您存款{count}成功')
    checkSum(False)


def main():
    print('---------主菜单----------')
    print(f"{name},您好，欢迎来到xx银行，请选择操作：")
    print('查询余额\t[输入1]')
    print('存款\t\t[输入2]')
    print('取款\t\t[输入3]')
    print('退出\t\t[输入4]')
    return input("请输入您的选择：")


while True:
    keyword_inpt = main()
    if keyword_inpt == '1':
        checkSum(True)
        continue
    if keyword_inpt == '2':
        num = int(input('请输入您要存款的金额：'))
        addMoney(num)
        continue
    if keyword_inpt == '3':
        getMoney()
        continue
    if keyword_inpt == '4':
        break


print('欢迎下次使用～')
