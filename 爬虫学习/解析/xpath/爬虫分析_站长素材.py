# 1、请求对象的定制
# 2、获取网页的源码
# 3、下载

# 解决抓取内容出现ssl错误问题
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 需求下载前10页的图片
# https://sc.chinaz.com/tupian/qinglvtupian.html
# https://sc.chinaz.com/tupian/qinglvtupian_2.html
import urllib.request
from lxml import etree
import urllib.request
import shutil
import os

def create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_' + str(page) + '.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request1):
    response = urllib.request.urlopen(request1)
    content = response.read().decode('utf-8')
    return content



def down_load(ctx):
    # urllib.request.urlretrieve('图片地址', '文件名字')
    tree = etree.HTML(ctx)
    name_list = tree.xpath('//div[@class="container"]//div//div/img/@alt')
    img_list = tree.xpath('//div[@class="container"]//div//div/img/@data-original')
    print(len(name_list), len(img_list))
    for i in range(len(name_list)):
        name = "./url/" + name_list[i] + '.jpg'
        src = 'https:' + img_list[i]
        result = urllib.request.urlretrieve(url=src, filename=name)
        print(result)


if __name__ == '__main__':
    start_page = int(input("请输入起始页码：") or 1)
    end_page = int(input("请输入结束页码：") or 1)

    for page in range(start_page, end_page + 1):
        # 1、请求对象的定制
        request = create_request(page)
        # 2、获取网页的源码
        content = get_content(request)
        # 3、下载
        down_load(content)
