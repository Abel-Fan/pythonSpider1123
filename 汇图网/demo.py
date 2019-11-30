import requests
# requests 网络请求包
from lxml import etree
import os
# lxml 识别 符合html语法的文本
kw = input('请输入爬取图片的关键字:')
wj = os.mkdir(kw)
url = "http://soso.huitu.com/search?kw=%s"%kw

response = requests.get(url)  # 获取 网址的响应 数据
# print(response.text)  # 获取网页源代码  str
# 获取网页源代码中的图片地址

html = etree.HTML(response.text)  # 识别网页源代码
# 获取图片网址的
arr = html.xpath("//div[@class='seozone']/a/img/@originalsrc")   # 选择元素|获取元素

num = 1
for imgURL in arr:
    res = requests.get(imgURL)  # 请求图片网址
    # res.content   # 图片的数据
    # 保存图片
    with open('%s/%s.jpg'%(kw,num),"wb") as f:
        f.write(res.content)
        num+=1



