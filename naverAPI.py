import requests, json
from bs4 import BeautifulSoup

url = "https://openapi.naver.com/v1/search/blog.json"

title = "파이썬"
params = {
    "query": title,
    "display": 100,
    "start": 1,
    "sort": "date"
}

headers = {
    "X-Naver-Client-Id": "oWaeXA0nme3FmIVx1h6o",
    "X-Naver-Client-Secret": "alfHVYo8xy"
}

result = requests.get(url, params=params, headers=headers).text

jsonData = json.loads(result)
# print(jsonData)
# print(json.dumps(jsonData, ensure_ascii=False, indent=2))

for item in jsonData['items']:
     print("게시글명: {}\n게시글 주소: {}\n블로거 이름: {}\n작성일: {}\n\n".format(item['title'], item['link'],
     item['bloggername'], item['postdate'])) 
    