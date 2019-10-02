from urllib import request
from urllib import parse

data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf-8')
# print(data)

response1 = request.urlopen('http://httpbin.org/post', data=data, timeout=1)
print(response1.read().decode('utf-8'))

print('-----------------')
response2 = request.urlopen('http://httpbin.org/get', timeout=1)
print(response2.read().decode('utf-8'))

import urllib
import socket

try:
    response3 = request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('timeeeee out')

# 模拟请求头
# headers = {
#     'accept': '',
#     'accept-Encoding': '',
#     'Connect': '',
#     'User-agent': ''
# }
# dict = {
#     'name': 'value'
# }
# data = bytes(parse.urlencode(dict, dict), encoding='utf=8')
# req = request.Request('http://httpbin.org/post', data=data, headers=headers, method='POST')
# response4 = request.urlopen(req)
# print(response4.read().decode('utf-8'))


# requests库使用
# get请求
# import requests
#
# url = 'http://httpbin.org/get'
# data = {'key': 'value', 'abc': 'xyz'}
# .get是使用get方式请求url，字典类型的data不用进行额外的处理
# response = requests.get(url, data)
# print(response.text)

# post请求

import requests

url = 'http://httpbin.org/post'
data = {'key': 'value', 'abc': 'xyz'}
response = requests.post(url, data)
# 返回类型为json格式
print(response.json())
