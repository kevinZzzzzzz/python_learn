import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request

url = 'https://www.baidu.com/s?wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

# # 模拟浏览器访问服务器
response = urllib.request.urlopen(request)
# proxies = {
#     'http': '123.169.39.212:9999'
# }
# handler = urllib.request.ProxyHandler(proxies = proxies)
# opener = urllib.request.build_opener(handler)
# response = opener.open(request)

content = response.read().decode('utf-8')

with open('proxy.html', 'w', encoding='utf-8')as fp:
    fp.write(content)
