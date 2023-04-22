# 解决抓取内容出现ssl错误问题
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request
url = 'https://www.baidu.com'

"""
    url的组成 协议 + 主机 + 端口号
    http        80
    https       443
    mysql       3306
    oracle      1521
    redis       6379
    mongodb     27017
"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
print(request)  #  <urllib.request.Request object at 0x10c5abc10>
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)

