from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint as pp
import csv, codecs

url = "https://www.melon.com/chart/index.htm"

headers = {
    'Referer' : 'https://www.melon.com/index.htm',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
} 

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, 'html.parser')

datanocnt = soup.select('#frm > div > table > tbody > tr[data-song-no]')

dic = {}
songsnum = []

for i in datanocnt:
    data_song_no = i.attrs['data-song-no']
    songsnum.append(data_song_no)
    rank = i.select_one('span.rank').text
    # rank = i.select_one('div.wrap.t_center').text.strip()
    songname = i.select_one('div.ellipsis.rank01').text.strip()
    singername = i.select_one('span.checkEllipsis').text.strip()
    dic[data_song_no]= {"rank" : int(rank), "songname" : songname, "singername" : singername, "likecnt" : 0} 
    

urljson = "https://www.melon.com/commonlike/getSongLike.json"

params = {
    'contsIds' : ','.join(songsnum)
}

htmlcnt = requests.get(urljson, params=params, headers=headers).text
jsonData = json.loads(htmlcnt)
strJson = json.dumps(jsonData, ensure_ascii=False, indent=2)

for j in jsonData['contsLike']:
    # print("jjj=", j)
    k = str(j['CONTSID'])
    # print(dic[k])
    dic[k]['likecnt'] = j['SUMMCNT']

print("===============================")
print(type(dic))

dicbyrank = sorted(dic.items(), key=lambda d: d[1]['rank']) #sorted 되면 튜플? list? 로 바뀌어 버림!
dicbylike = sorted(dic.items(), key=lambda d: d[1]['likecnt'])
print(type(dicbylike))

v_leastlike = dicbylike[0][1]['likecnt']
# print(v_leastlike)

with codecs.open('./data/output.csv', 'w', 'euc-kr') as ff:
    writer = csv.writer(ff, delimiter=',', quotechar='"')
    writer.writerow(['순위', '노래제목', '가수', '좋아요1', '좋아요2'])  
    likecntsum = 0
    likecntsum2 = 0

    for cell in dicbyrank:
        s = cell[1]
        print(type(s))
        likecnt2 = s['likecnt']-v_leastlike
        likecntsum += s['likecnt']
        likecntsum2 += likecnt2
        writer.writerow([s['rank'], s['songname'], s['singername'], s['likecnt'], likecnt2])  
        
    writer.writerow(['총계', '', '', likecntsum, likecntsum2])  



