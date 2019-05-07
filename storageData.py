import requests
from bs4 import BeautifulSoup
link = "http://www.santostang.com"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/70.0.3538.67   Safari/537.36'}
r = requests.get(link ,headers=headers)

soup = BeautifulSoup(r.text, "lxml")
title = soup.find("h1" ,class_="post-title").a.text.strip()
print(title)
with open('title.txt', "a") as f: # with open("文件名","mode")   mode=a  万能的a 不清空连续写入 mode=r 只读,如果文件不存在会发生异常 mode=w 只写 如果文件不存在 则创建
                                                # 存在则覆盖 mode=rb 以二进制读文件 wb 二进制写  rt 文本读  wt 文本写 rb+以二进制读打开  可读写 文件不存在则异常 wb+以二进制写打开  可读写
    f.write("\n------------------我是分割线--------------------\n")
    f.write(title)
    f.close()