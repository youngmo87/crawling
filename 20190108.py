from bs4 import BeautifulSoup
import requests

url = "https://external-icn1-1.xx.fbcdn.net/safe_image.php?d=AQAHXx4ggdnxlUFa&w=540&h=282&url=http%3A%2F%2Ftoday-issue.com%2Fwp-content%2Fuploads%2F2019%2F01%2Fthumbnail-26.jpg&cfs=1&upscale=1&fallback=news_d_placeholder_publisher&_nc_hash=AQAIvBQ9SLI5j5-Q"
img = requests.get(url).content
 
with open("./webcrawl/"+ "aaa.png", mode="wb") as file:
    file.write(img)

print("OK!")