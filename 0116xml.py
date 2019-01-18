from bs4 import BeautifulSoup
import requests

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp"

res = requests.get(url)

with open("kma.xml", "w", encoding="utf-8") as f:
    f.write(res.text)

soup = BeautifulSoup(res.text, "html.parser")
title = soup.select('item title')
print(soup)

data = soup.select('body data')

# XML을 저장했을때에는 소문자로 바뀐다! soup.select를 할때 소문자로 바꿔줄것!
