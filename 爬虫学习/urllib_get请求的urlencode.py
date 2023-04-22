# 解决抓取内容出现ssl错误问题
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request
import urllib.parse

#  urlencode应用场景：多个参数
# https://www.baidu.com/s?wd=周杰伦&sex=男
base_url = 'https://www.baidu.com/s?'
data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}
a = urllib.parse.urlencode(data)
print(a)
# 请求对象地址
url = f'{base_url}{a}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
print(request)
response = urllib.request.urlopen(request)
context = response.read().decode('utf-8')
# print(context)
# f = open('search.html', 'a', encoding='utf-8')
# f.write(context)
# f.close()





