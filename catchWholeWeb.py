import requests

link = "http://www.taobao.com"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/70.0.3538.67   Safari/537.36'}
r = requests.get(link, headers= headers)
print(r.headers)
print(r.cookies)
print(r.elapsed)
print(r.encoding)
print(r.text)

