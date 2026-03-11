# 字符串索引和切片
# 索引：按照位置提取元素
s = '我叫kevinzzzzzz'

print(s[0], s[2], s[-1])


# 切片
# 从字符串中提取一部分内容
s1 = '我叫周杰伦，你叫周润发么？'
print(s1[3:5])

print(s[:7])
print(s[:])


# 给切片添加步长，控制切片方向
print(s1[::-1])

# 字符串的常规操作
s2 = 'python'
s3 = s2.capitalize()  # 首字母大写
print(s3)

s4 = 'I have a dream'
s5 = s4.title()  # 每个单词首字母大写
print(s5)

s6 = 'I HAVE A DREAM'
s7 = s6.lower()  # 每个单词变小写
print(s7)

s8 = 'i have a dream'
s9 = s8.upper()  # 每个单词变大写

print(s9)


# 替换和切割
s10 = '   你好,    我叫   周杰伦   '
s11 = s10.strip()  # 去掉前后的空格或者\t \n
print(s11)
s12 = s10.replace(' ', '')  # 把所有空格替换
print(s12)

s13 = 'python_java_c#_javascript'
s14 = s13.split('_')  # 字符串切割成list
print(s14)



# 查找和替换
s15 = '你好啊，我叫周润发'
s16 = s15.find('周润发')  # 返回-1表示不存在
print(s16)

s17 = s15.index('周润发') # 报错表示不存在
print(s17)

# in 可以做条件上的判断  => bool
print('周润' in s15)  # True
print('周润发123' not in s15)  # True



# 判断
name = input('请输入你的名字:')
# 判断你的是不是姓张
if name.startswith('张'):
    print('YSE')
else:
    print('NO')

money = input('请输入你兜里的钱:')
if money.isdigit():  # 判断字符串是否由整数组成
    money = int(money)
    print('你可以花钱了')
else:
    print('对不起，您的输入有误。。。')


# list => str
l18 = ['haha', 'hehe', 'eenen']
s18 = '_'.join(l18)  # 用_链接
print(s18)
