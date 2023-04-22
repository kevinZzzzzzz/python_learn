# 解决抓取内容出现ssl错误问题
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import json
import jsonpath
import urllib.request

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1687104380747_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers = {
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'h-CN,zh;q=0.9',
    'Bx-V': '2.5.0',
    'Cookie': 'cna=zoNUG34G52gCAXF2XPua22wz; linezing_session=xk4PaEaCEx67ul21477cYaNg_1686752427901nyEb_1; '
              'cookie2=1904ca20a3a03b6dc84c3902b6d59f43; t=5197b13fa73293faa323c6106f0323c4; _tb_token_=5bb1bf6e181fd; '
              '_m_h5_tk=fb137df42a4e19e1df4101f909e18985_1686760351252; _m_h5_tk_enc=21696b72035bbc0471b185c1303cc649; '
              '_samesite_flag_=true; xlly_s=1; v=0; '
              'isg=BCYmjnGUfj5Hxypaz5xOfgLrd5qoB2rB8H5bwhDPtckkk8ateJYt0Udl648fO2LZ; '
              'tfstk=drAJn_AALqU-o1uKZgH08hRn1QumIQLrr38_tMjudnKvb33PK8vkpkIv54SoLY'
              '-pHHtVEgOp8WQBRHuPx4kDzU5FOcmM9fYyzi3qjc2fi5ocT6iij-VCUfCefiC7xGfiLWNUy7tWsaML4an'
              '-TO4PPTI6kAPQ9ub7jGTSZWFpMKBRQrOM6oW4jGQ3Fq3YLJW5uyBePx5..; '
              'l=fB_bJ5bnNsZoT2hfBO5Cnurza77tVIRb4sPzaNbMiIEGa1PRtFwyXNC1tgLXSdtjgTCbietPl_pr6dLHRnO0hc0c07kqm05j3xvtaQtJe',
    'Referer': 'https://dianying.taobao.com/',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': 'macOS',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

content = content.split('(')[1].split(')')[0]
print(content)
with open('data1.json', 'w', encoding="utf-8") as fp:
    fp.write(content)

# 获取地名
obj = json.load(open('data1.json', 'r', encoding='utf-8'))
city_list = jsonpath.jsonpath(obj, '$.returnValue..regionName')
print(city_list)


