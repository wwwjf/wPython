import requests
from bs4 import BeautifulSoup

url = 'http://sz.lianjia.com/zufang'
response = requests.get(url)
print(response.text)
