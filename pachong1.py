from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# url = 'http://www.baidu.com'
# url = "http://www.ly6080.com.cn/index.php/vod/play/id/9030/sid/1/nid/9.html"
url = "http://www.ly6080.com.cn/index.php/vod/play/id/9030/sid/1/nid/10.html"


response = request.urlopen(url, timeout=10)
print(response.read().decode('utf-8'))


