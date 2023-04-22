# 解决抓取内容出现ssl错误问题
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request

url = 'https://weibo.cn/2094873042/info'
headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Client-Version': 'v2.40.50',
'Cookie': 'SCF=Ap9EbSmGBoLI_9z1KwaosxgbCEqQ4vVs3aMnbHs2a0ZXQyeiui_LPNUeoLE0QBAeN2As3Q0xjGU4LYQg8c5Tcso.; SUB=_2A25JZOd8DeRhGeRO4lYZ9y3Mzz6IHXVqpok0rDV6PUNbktAGLW7WkW1NUEslJDsU3Q0lyNMTl537qBeLo6Yv4hWY; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWTiRoZ06i7v3eATCwyEFzJ5JpX5KMhUgL.Foz71KBRS0e7Shz2dJLoIpjLxK-LB.eLBo-LxKqL1KnLBK5LxK-L1hzL1K2t; SSOLoginState=1684051756; ALF=1686643756; _T_WM=be03eb53945edb56cccf0dbb6604a7a6',
'Referer': 'https://weibo.cn',
'Sec-Ch-Ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
'Sec-Ch-Ua-Mobile': '?0',
'Sec-Ch-Ua-Platform': 'macOS',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'Server-Version': 'v2023.05.11.1',
'Traceparent': '00-9eee828d70aa437efc7c7797007e9cbf-7cc9711390073cf8-00',
'X-Requested-With': 'XMLHttpRequest',
'X-Xsrf-Token': 'A_B-UjLGjxA3BfikhKfFquUa',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')


with open('weibo.html', 'w', encoding='utf-8')as fp:
    fp.write(content)
