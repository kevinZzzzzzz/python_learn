# 解决抓取内容出现ssl错误问题
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request

#  下载网页
url_page = 'http://www.baidu.com'
#  url 代表的是下载的路径 filename文件名
urllib.request.urlretrieve(url_page, '百度.html')
#  下载图片
url_image = 'https://img2.baidu.com/it/u=260211041,3935441240&fm=253&fmt=auto&app=120&f=JPEG?w=800&h=800.jpg'
urllib.request.urlretrieve(url=url_image, filename='百度logo.jpg')
#  下载视频
url_video = 'https://www.ixigua.com/f65d80bc-1c63-41fb-ae5e-e13785422e89'
urllib.request.urlretrieve(url=url_video, filename='视频.mp4')
