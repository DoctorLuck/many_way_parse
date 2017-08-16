#coding : utf-8
import requests
import re
from multiprocessing.dummy import Pool
import json




# 爬取内涵段子网


urlList=[]
baseUrl='http://www.neihan8.com/article/list_5_%s.html'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}


def makePage():
    for i in range(1,10):
        # print(baseUrl%str(i))
        # urlList.append(baseUrl%str(i))
        # print(baseUrl%str(i))
        load(baseUrl%str(i))
def load(url):
    r=requests.get(url,headers=headers)
    r.encoding='gbk'

    # print(url)
    text=r.text
    # print(text)
    pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>',re.S)
    item_list=pattern.findall(text)
    for item in item_list:
        print(item.lstrip('\u3000').strip().replace('<p>','').replace('</p>','').replace('<br />','').replace('&rdquo','').replace('&ldquo','').replace('&hellip','').replace('\n','').strip())
makePage()
# r=requests.get()
# print(urlList)


