import requests
from lxml import etree

# 推导式
# # 列表推导式
urls = [ "https://movie.douban.com/top250?start=%s"%i for i in range(0,226,25)]
response = requests.get(urls[0],headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
})
html = etree.HTML(response.text)
titles = html.xpath("//div[@class='item']/div[@class='info']/div/a/span[1]/text()")
print(titles)
