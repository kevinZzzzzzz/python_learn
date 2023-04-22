
# 解决抓取内容出现ssl错误问题
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 获取网页的源码
# 解析  解析服务器响应的文件 etree.HTML

import urllib.request

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 解析网页源码 来获取想要的数据
from lxml import etree
tree = etree.HTML(content)
# 获取想要的数据 xpath的返回值就是一个列表
result = tree.xpath('//input[@id="su"]/@value')
print(result) # ['百度一下']


