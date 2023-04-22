# 解决抓取内容出现ssl错误问题
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
# 将汉字转换成unicode编码格式
name = urllib.parse.quote('周杰伦')
print(name)
# 百度查询周杰伦
url = f'https://www.baidu.com/s?wd={name}'

# 请求对象的地址
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取响应的内容
context = response.read().decode('utf-8')
print(context)
f = open('search.html', 'a', encoding='utf-8')
f.write(context)
f.close()
