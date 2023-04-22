# 解决抓取内容出现ssl错误问题
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 使用urlib来获取百度首页源码
import urllib.request

# 定义一个url
URL = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求  response响应
response = urllib.request.urlopen(URL)
# 获取响应中页面的源码  read方法返回的是字节形式的二进制数据
# 解码将二进制转化为字符串 decode()
content = response.read().decode('utf-8')
print(content)

