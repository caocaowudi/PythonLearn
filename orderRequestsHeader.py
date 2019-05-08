import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/70.0.3538.67 Safari/537.36', 'Host': 'www.taobao.com'}

r = requests.get(' http://www.taobao.com', headers=headers)

#  r = requests.get(' http://www.taobao.com', timeout=0.01)
#    raise ReadTimeout(e, request=request)
# requests.exceptions.ReadTimeout: HTTPSConnectionPool(host='www.taobao.com', port=443): Read timed out. (read
# timeout=0.01)

print("响应状态码:", r.status_code)
