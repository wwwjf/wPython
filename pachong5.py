from bs4 import BeautifulSoup
import requests
import os
from pathlib import Path
import shutil

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; "
              "_gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://www.infoq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

url_news = 'http://www.infoq.com/cn/news'


def craw(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    for title_href in soup.find_all('div', class_='news_type_block'):
        print([title.get('title') for title in title_href.find_all('a') if title.get('title')])


# 获取新闻标题
# for i in range(15, 150, 15):
#     url2 = url_news + '/' + str(i)
#     craw(url2)


url_picture = 'http://www.infoq.com/cn/presentations'


def download_img(url_img, path_img):
    response = requests.get(url_img, stream=True)
    if response.status_code == 200:
        with open(path_img, 'wb') as f:
            response.raw.deconde_content = True
            shutil.copyfileobj(response.raw, f)


# 下载图片
def craw2(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    for pic_href in soup.find_all('div', class_='news_type_video'):
        for pic in pic_href.find_all('img'):
            url_img = pic.get('src')
            dir = os.path.abspath('./pic')
            if os.path.exists(dir) is False:
                directory = Path(dir)
                Path.mkdir(directory, parents=True)
            filename = os.path.basename(url_img)
            path_img = os.path.join(dir, filename)
            print('url_img=' + url_img + '\npath_img=' + path_img)
            download_img(url_img, path_img)


craw2(url_picture)
