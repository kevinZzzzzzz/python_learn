import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)

# content = response.readline() # 读取一行

# content = response.readlines() # 读取输出list

content = response.getcode()  # 获取状态码
print(content)

print(response.geturl())  # 放回url

print(response.getheaders())  # 获取请求头
