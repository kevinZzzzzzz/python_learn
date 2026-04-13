'''
日志记录
1、用户输入用户名和密码后，程序进行校验
2、用户名不存在，提示 用户名未注册，并记录日志
3、用户名存在，但密码错误，提示 密码错误  记录日志
4、用户名和密码正确，提示 登录成功 记录日志
'''
import time
users = {
    '张三': '123456',
    '李四': '888888',
    '王五': 'abc123'
}
now = time.strftime('%Y-%m-%d %H:%M:%S')
username = input('请输入用户名：')
password = input('请输入密码：')

# 如果用户名不再user
if username not in users:
    print('用户名未注册')
    with open('dome/aa/bb/cc/log.txt', 'at', encoding='utf-8') as f1:
        f1.write(f'{now} {username}登录失败，用户未注册\n')
elif users[username] != password:
    print('密码不正确')
    with open('dome/aa/bb/cc/log.txt', 'at', encoding='utf-8') as f2:
        f2.write(f'{now} {username}登录失败，密码不正确\n')
else:
    print('登录成功！')
    with open('dome/aa/bb/cc/log.txt', 'at', encoding='utf-8') as f2:
        f2.write(f'{now} {username}登录成功\n')
