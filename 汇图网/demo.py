import requests
from lxml import etree
# lxml 识别html 文本

url = 'http://soso.huitu.com/search?kw=猫'
response = requests.get(url)

html = etree.HTML(response.text)
# 所有的图片网址
arr = html.xpath("//div[@class='seozone']/a/img/@originalsrc")

num = 1
for url in arr:
    print("正在保存第%s张图片"%num)
    res = requests.get(url)
    with open("%s.jpg"%num,"wb") as f:
        f.write(res.content)
        num+=1