
from bs4 import BeautifulSoup

# 通过解析本地文件，将bs4的基础语法进行讲解
# 默认格式是gbk，需要指定编码
soup = BeautifulSoup(open('基本使用.html', encoding='utf-8'), 'lxml')
# print(soup)

# 根据标签查找元素
# 查找的是第一个符合条件的数据
print(soup.a)
print(soup.a.attrs) # 获取标签的属性和属性值

# bs4的一些函数
    # find
# 返回第一个返回的数据
print(soup.find('a'))
# 根据title的值找到标签对象，注意的是class需要加下划线
print(soup.find('a', title='a2'))
print(soup.find('a', class_='a1'))
    # find_all
print(soup.find_all('a'))  # [<a class="a1" herf="" id="">马六</a>, <a herf="" title="a2">马六</a>]
# 获取多个需要传入list
print(soup.find_all(['a', 'span']))
print(soup.find_all('li', limit=2))
    # select
print(soup.select('a'))
print(soup.select('.a1'))
print(soup.select('#a11'))
print(soup.select('li[id]'))
# 查找到id为l2的元素
print(soup.select('li[id="l1"]'))
# 层级选择器
print(soup.select('div li'))
print(soup.select('div a'))
# 子代选择器
print(soup.select('div > ul > a'))
# 获取多个元素
print(soup.select('a,li'))

# 获取节点信息
obj = soup.select('#d1')
print(obj[0].string)
print(obj[0].getText())

# 节点属性
obj = soup.select('#p1')
print(obj[0].name)  # name是标签的名字
print(obj[0].attrs)
print(obj[0].get('class'))


