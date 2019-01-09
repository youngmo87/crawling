import urllib.request as ur

url = "http://www.weather.go.kr/repositary/image/rdr/img/RDR_CMP_WRC_201901081250.png"

saveFile="./webcrawl/test1.png"
ur.urlretrieve(url, saveFile)
print("OK!")

