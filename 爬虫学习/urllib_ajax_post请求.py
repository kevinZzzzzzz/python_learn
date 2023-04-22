import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request
import urllib.parse
import json


# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 北京
# pid:
# pageIndex: 1
# pageSize: 10
def create_request(sPage, apart):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    data = {
        'cname': apart,
        'pid': '',
        'pageIndex': sPage,
        'pageSize': 10
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url=base_url, data=data, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')

    # fp = open(f'data{sPage}.json', 'w', encoding='utf-8')
    # fp.write(content)
    # fp.close()
    with open(f'kfc{sPage}.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))
    apart = str(input('请输入查询城市：'))

    for page in range(start_page, end_page + 1):
        context = create_request(page, apart)
