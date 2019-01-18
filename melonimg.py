from bs4 import BeautifulSoup
import requests
import urllib.parse as parse
import os.path as path
import urls


url = "https://www.melon.com/chart/index.htm"

headers = {
    'Referer' : 'https://www.melon.com/index.htm',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
} 

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, 'html.parser')

sel = soup.select('#frm > div > table > tbody > tr[data-song-no]')
for i in sel:
    images = i.select_one('img')    
    src=images.get('src')
    # print("img>>", src)
    with open("./images/" + i.select_one('span.rank').text + ".png", "wb") as file:
        file.write(requests.get(src).content)

    
    
    
    
    # for img in images:
    #     print('a')
    #     src = img.get('src')
    #     print("img>>", src)
        # with open("./images/" + urls.getFilename(src), "wb") as file:
            # file.write(requests.get(src).content)
