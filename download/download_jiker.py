# -*- coding:utf-8 -*-
# 爬虫分析极客学院学习视频网站，并下载视频
import requests
import json
import os
from pathlib import Path

url_data_list = 'http://course.jiker.com/api/web/course?page=1&page_size=12&sort_type=time&difficulty_level=0'
# url_data_detail = 'https://course.jiker.com/api/web/course/130?type=lesson'
url_data_detail = 'http://course.jiker.com/api/web/course/{0}?type=lesson'
# url_data_video = 'https://learn.jiker.com/course/130/4453/4454'
url_data_video = 'http://learn.jiker.com/course/{0}/{1}/{2}'
headers = {
    'Accept':'application/json',
    # 'Set-Cookie':'QINGCLOUDELB=dd91b9e2eaabd29b1d0bac5e684e6c7e466d62c936b443a78592d63b6f4b026e|XqxQN|XqxQN; path=/; HttpOnly',
    'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODc1NjUzODAsImlzcyI6Imh0dHBzOlwvXC9wYXNzcG9ydC5qaWtlci5jb20iLCJleHAiOjE1OTAxNTczODAsImF1ZCI6Imh0dHBzOlwvXC9qaWtlci5jb20iLCJzdWIiOjIzNjEsImluZm8iOnsiaWQiOjIzNjEsIm5hbWUiOiJqaWtlcjI1Njg5MDMiLCJjb3VudHJ5X2NvZGUiOiI4NiIsInBob25lX251bWJlciI6IjE1NjU5MDI1NzkwIiwiaW52aXRlX3VzZXJfaWQiOjB9fQ.UfWsrKN2H6pfbyGW8XOvnYgASp5cE3R3aVFRekjE8X8',
    'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}


def request_http(url):
    response = requests.get(url,headers=headers)
    return json.loads(response.text)

def video_save(id_course,id_lesson,lesson_child):
    response = requests.get(lesson_child['url'])
    dir = os.path.abspath('./{0}'.format(id_course))
    if os.path.exists(dir) is False:
        directory = Path(dir)
        Path.mkdir(directory, parents=True)
    videoName = '{0}/{1}_{2}_{3}.mp4'.format(id_course, id_lesson, lesson_child['id'], lesson_child['name'])
    if os.path.exists(videoName) is True:
        return
    # print('{0}文件不存在'.format(videoName))
    with open(videoName, 'wb') as f:
        f.write(response.content)
        f.flush()
        print('{0} success'.format(videoName))

# 单个课程详情
def request_detail(id):
    response_detail = request_http(url_data_detail.format(id))
    id_course = response_detail['data']['course']['id']
    list_lesson = response_detail['data']['course']['content']
    for lesson in list_lesson:
        list_lesson_child = lesson['children']
        # print(list_lesson_child)
        for lesson_child in list_lesson_child:
            id_lesson_child = lesson_child['id']
            # print(len(lesson_child['url']))
            # if id_lesson_child != 4454:
            #     continue
            video_save(id_course,lesson['id'],lesson_child)



# 课程列表
loadData_response = request_http(url_data_list)
data_list = loadData_response['data']['list']
for item in data_list:
    if not(item['is_vip']):
        request_detail(item['id'])
print('end')
