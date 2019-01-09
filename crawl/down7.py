import os
import urllib.request as ur
from urllib import parse
from bs4 import BeautifulSoup
import requests

url = "https://blog.naver.com/PostView.nhn?blogId=korea_diary&logNo=221433346994&redirect=Dlog&widgetTypeCall=true&directAccess=false"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

def getFileName(url) :
    p = parse.urlparse(url).path
    return path.basename(p)

sel = "#SE-9311ee77-8bde-4b1f-9e02-7ea73e016f1f > div > div > a > img"
# sel = "img.se-image-resource"

imgs = soup.select(sel)
print(imgs, len(imgs))

if len(imgs) < 1:
    exit()

print("--------------------------------------")
for img in imgs:
    url = img.get('src')
    saveFile = "./images/test2.png"
    mem = ur.urlopen(url).read()
    with open(saveFile, mode="wb") as file:
        file.write(mem)

print("OK!")







print("OK!")
