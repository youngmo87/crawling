from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/marketindex/exchangeList.nhn"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())
trs = soup.select('tbody')

# print(trs)

for tr in trs:
    tds=tr.select_one('td')
print(tds)  

# print(trs[0])


# tds=tr.select(td)
# for td in tds

# sel = "img.se-image-resource"

# foreign = "td.tit"
# foregins = soup.select(foreign)

# for tr in trs:
#     src = tr.get('src')
#     print("img>>", src)
#     with open("./images/" + urls.getFilename(src), "wb") as file:
#         file.write(requests.get(src).content)



# usd = soup.select("#exchangeList > li:nth-of-type(1) > a.head.usd > div > span.value").text
# print("usd=", usd, float(usd.replace(',', '')))


# usd = soup.select_one("#exchangeList > li:nth-of-type(1) > a.head.usd > div > span.value").text
# print("usd=", usd, float(usd.replace(',', '')))


# sel = "#SE-9311ee77-8bde-4b1f-9e02-7ea73e016f1f > div > div > a > img"




