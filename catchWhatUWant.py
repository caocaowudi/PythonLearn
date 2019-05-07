import requests
from bs4 import BeautifulSoup

link = "http://www.taobao.com"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/70.0.3538.67   Safari/537.36'}
r = requests.get(link, headers=headers)

soup = BeautifulSoup(r.text, "lxml")  # 使用BeautifulSoup来解析这段代码
ttile = soup.find("div",class_="search-hots-fline").a.text.strip()
print(ttile)