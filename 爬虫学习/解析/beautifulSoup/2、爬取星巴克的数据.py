# 解决抓取内容出现ssl错误问题
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request

url = 'https://www.starbucks.com.cn/menu/'
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')

from bs4 import BeautifulSoup
soup = BeautifulSoup(content, 'lxml')
name_list = soup.select('ul[class="grid padded-3 product"] strong')
print(name_list)

for i in name_list:
    print(i.getText())
