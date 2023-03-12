"""
函数的定义:
def 函数名(参数):
    函数体
    return 返回值

使用步骤
    先定义函数
    后调用函数
"""
# 统计字符串长度
str1 = 'hahahahahah'
str2 = 'heehe'
str3 = 'enenenen'


def lens(date):
    count = 0
    for i in date:
        count += 1
    print(f'字符串{date}的长度是：{count}')


lens(str1)
lens(str2)
lens(str3)
