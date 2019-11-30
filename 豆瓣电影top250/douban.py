import requests
from lxml import etree
# 推导式
# # 列表推导式
urls = [ "https://movie.douban.com/top250?start=%s"%i for i in range(0,226,25)]

def getPageData(url):
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

    # rating_num
    rats = html.xpath("//div[@class='star']/span[2]/text()")

    # inq
    inqs = html.xpath("//p[@class='quote']/span/text()")

    pageData = list(zip(titles,dirs,rats,inqs))
    print(pageData)

getPageData(urls[1])