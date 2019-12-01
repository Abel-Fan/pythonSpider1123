import requests
from lxml import etree
import time,random
# 推导式
# # 列表推导式
urls = [ "https://movie.douban.com/top250?start=%s"%i for i in range(0,226,25)]

data = []

def getPageData(url):
    global data
    # time.sleep(random.randint(0,3))
    print("%s正在爬取..."%url)
    response = requests.get(url,headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    })
    html = etree.HTML(response.text)
    # 标题
    titles = html.xpath("//div[@class='item']/div[@class='info']/div/a/span[1]/text()")

    # 导演
    dirs = html.xpath("//div[@class='item']/div[@class='info']/div[@class='bd']/p[1]/text()")
    # dirs list
    dirs = [ s.strip() for s in dirs]
    dirs2 = []
    for i in range(0,50,2):
        dirs2.append(dirs[i]+dirs[i+1])


    # rating_num
    rats = html.xpath("//div[@class='star']/span[2]/text()")

    # inq
    inqs = html.xpath("//div[@class='info']/div[@class='bd']")
    inqs2 = []
    for item in inqs:
        zt = item.xpath("./p[contains(@class,'quote')]/span/text()")
        if len(zt)>0:
            inqs2.append(zt[0])
        else:
            inqs2.append("")



    pageData = list(zip(titles,dirs2,rats,inqs2))
    data += pageData


for i in urls:
    getPageData(i)

import pickle
with open("dbData.txt","wb") as f:
    pickle.dump(data,f)