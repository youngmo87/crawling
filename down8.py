from bs4 import BeautifulSoup
import requests
import urls

bbsUrl = "https://blog.naver.com/korea_diary/221433346994"
html = requests.get(bbsUrl).text
soup = BeautifulSoup(html, 'html.parser')

ifrSel = "iframe#mainFrame"
ifr = soup.select_one(ifrSel)
src = ifr.get('src')
orgUrl = urls.urljoin( urls.getHostname(bbsUrl, True), src )

orgHtml = requests.get(orgUrl).text
orgSoup = BeautifulSoup(orgHtml, 'html.parser')

titleSel = "div.se-title-text span"
title = orgSoup.select_one(titleSel).text

sel = "img.se-image-resource"
imgs = orgSoup.select(sel)
# print(imgs, len(imgs))

if len(imgs) < 1:
    exit()

print("--------------------------------------", title)
for img in imgs:
    src = img.get('src')
    print("img>>", src)
    with open("./images/" + urls.getFilename(src), "wb") as file:
        file.write(requests.get(src).content)

#    res = requests.get(site)
#    soup = BeautifulSoup(res.text, 'html.parser')
#    sel_2 = "div.se-title-text"
#    texts = soup.select(sel_2)[0].text
#    save_name = "2.csv"
#    with open(save_name, mode="w") as file:
#        file.write(texts)