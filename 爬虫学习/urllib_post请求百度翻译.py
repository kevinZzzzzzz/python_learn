#  post请求
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request
import urllib.parse
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
url = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'spider'
}
# post请求的参数必须进行编码.encode('utf-8')
data = urllib.parse.urlencode(data).encode('utf-8')
print(data)
# 请求参数是放置在请求定制的方法中的
request = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content, type(content))

obj = json.loads(content)
print(obj)
