def add(a, b):
    result = a + b
    return result


add1 = add(1, 2)
add2 = add(3, 4)
print(add1, add2)


# test 自动查温度
def checkTemp():
    print('欢迎来到xxx，请出示您的健康码以及72小时核酸证明，并配合测量体温！')
    temp = float(input('请输入您的温度：'))
    if temp <= 37.6:
        print(f"体温测量中，您的体温是：{temp}度，体温正常请进！")
    else:
        print(f"体温测量中，您的体温是：{temp}度，需要隔离！")


checkTemp()
