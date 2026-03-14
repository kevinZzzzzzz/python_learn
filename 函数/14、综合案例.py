"""
完成一个健身挑战
记录7天的数量，并且总结
"""

# def record():
#     day = 1
#     amount = 0
#     ava = 0
#     while day <= 7:
#         result = int(input(f"第{day}天: "))
#         day += 1
#         amount += result
#     ava = amount / day
#     print("【仰卧起坐】【7天】健身总结总数%d, 平均值：%.1f" % (amount, ava))
#
# record()


amount = 0
day = 1
def calc_total(num):
    """
    统计总量
    :param num:
    :return:
    """
    global amount
    amount += num
    return amount
def calc_avg():
    """
    统计平均量
    :return:
    """
    return amount / day
def check_success():
    avg = calc_avg()
    print("""
    【仰卧起坐】【7天】健身总结
        总数%d, 平均值：%.1f
        挑战成功
    """ % (amount, avg)
          )
def check_fail():
    print("不好意思，挑战失败")

# def main():
#     while day <= 7:
#         num = int(input(f"第{day}天："))
#         if num <= 0:
#             check_fail()
#             break
#         else:
#             day += 1
#             calc_total(num)
#     if day > 7:
#         check_success()
#     print("谢谢您的参加")
def main():
    global day
    for i in range(7):
        num = int(input(f"第{day}天："))
        if num <= 0:
            check_fail()
            break
        else:
            day += 1
            calc_total(num)
    if day > 7:
        check_success()
    print("谢谢您的参加")


main()
