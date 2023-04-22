
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# get请求
# 获取豆瓣电影的第一页数据，并保存起来
import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)
context = response.read().decode('utf-8')
print(context)


# 数据下载到本地
fp = open('data.json', 'w', encoding='utf-8')
fp.write(context)
fp.close()
