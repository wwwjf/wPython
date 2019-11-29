from urllib.request import Request, urlopen
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 深圳中级人民法院
url = "http://www.szcourt.gov.cn/"

headers = {'User-Agent': 'Mozilla/5.0 3578.98 Safari/537.36'}
url = Request(url, headers=headers)
# 抓取数据e
content = urlopen(url, timeout=15).read()
print(content.decode('utf-8'))
