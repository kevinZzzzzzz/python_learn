import json
# 数据下载到本地


import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request
import urllib.parse

def create_request(sPage):

    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    data = {
        'start': (sPage - 1) * 20,
        'limit': 20
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    context = response.read().decode('utf-8')
    return context
import json
if __name__ == '__main__':
    start_page = int(input('请输入起始的页面'))
    end_page = int(input('请输入结束的页面'))
    dataList = []
    for page in range(start_page, end_page+1):
        context = create_request(page)
        # context = json.loads(context)
        # dataList.extend(context)

        # 数据下载到本地
        fp = open(f'data{page}.json', 'w', encoding='utf-8')
        fp.write(context)
        fp.close()
    print(dataList)




