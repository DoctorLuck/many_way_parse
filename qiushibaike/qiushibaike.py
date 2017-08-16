import json
import requests
from lxml import etree

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}




url='https://www.qiushibaike.com/8hr/page/1/'

r=requests.get(url,headers=headers)
html=etree.HTML(r.text)
content=html.xpath('//div[@class="content"]/span/text()')
# print(content)
for i in content:
    print(i.replace('\n',''))
