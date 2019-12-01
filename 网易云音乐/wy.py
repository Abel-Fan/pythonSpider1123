import requests
from lxml import etree
import json
url = "https://music.163.com/artist?id=2116"

response = requests.get(url,headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
})
html = etree.HTML(response.text)
songList = html.xpath("//textarea[@id='song-list-pre-data']/text()")[0]
# json

songData = json.loads(songList)

url2 = "http://music.163.com/song/media/outer/url?id=%s.mp3"
for song in songData:
    songName = song['name']  # 歌曲名
    songID = song['id'] # 歌曲id
    res = requests.get(url2%songID,headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
})
    print("正在下载%s"%songName)
    with open("songs/%s.mp3"%songName,"wb") as f:
        f.write(res.content)


