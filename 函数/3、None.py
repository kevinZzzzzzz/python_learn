"""
    None表示：空的，无实际意义的意思，无返回值函数
    函数没有return 任何东西，
    可用在if判断上
        在if判断上， None等同于False
                    not None 等同于 True
        一般用于字啊函数中主动返回None，配合if判断做相关处理
"""


def checkAge(age):
    if age > 18:
        return "success"
    else:
        return None


result = checkAge(16)
if not result:
    print('未成年，不可以进入')
else:
    print("请进")

# None 用于声明无初始化内容的变量
name = None
name = 2
