"""
当程序遇到不符合预期情况，可以使用raise语句手动触发（抛出）异常
"""
print('欢迎使用年龄判断系统')
try:
    age = int(input('请输入你的年龄：'))
    if 18 <= age <= 120:
        print('成年')
    elif 0 <= age < 18:
        print('未成年')
    else:
# print('输入的年龄有误！应该在0～120')
#         手动抛出异常
        raise ValueError('输入的年龄有误！应该在0～120')
except Exception as e:
    print('处理异常逻辑', e)
