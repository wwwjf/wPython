# -*- coding:utf-8 -*-
# 爬虫分析极客学院学习视频网站，并下载视频
import requests
import json
import os
from pathlib import Path

url_data_list = 'https://course.jiker.com/api/web/course?page={0}&page_size=12&sort_type=time'
# url_data_detail = 'https://course.jiker.com/api/web/course/130?type=lesson'
url_data_detail = 'https://course.jiker.com/api/web/course/{0}?type=lesson'
# url_data_video = 'https://learn.jiker.com/course/130/4453/4454'
url_data_video = 'https://learn.jiker.com/course/{0}/{1}/{2}'
path_video_jiker = '/users/wengjianfeng/movies/jiker'
headers = {
    'Accept': 'application/json',
    'Set-Cookie': 'QINGCLOUDELB=dd91b9e2eaabd29b1d0bac5e684e6c7e466d62c936b443a78592d63b6f4b026e|XuYBn|XuYBn; path=/; HttpOnly',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTIxMzEwNDUsImlzcyI6Imh0dHBzOlwvXC9wYXNzcG9ydC5qaWtlci5jb20iLCJleHAiOjE1OTQ3MjMwNDUsImF1ZCI6Imh0dHBzOlwvXC9qaWtlci5jb20iLCJzdWIiOjIzNjEsImluZm8iOnsiaWQiOjIzNjEsIm5hbWUiOiJqaWtlcjI1Njg5MDMiLCJjb3VudHJ5X2NvZGUiOiI4NiIsInBob25lX251bWJlciI6IjE1NjU5MDI1NzkwIiwiaW52aXRlX3VzZXJfaWQiOjB9fQ.Y2gFu45HmgHRCBW4uzBRItSSGwl_RI3Fqi5zhdOOvDI',
    'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}


def request_http(url):
    response = requests.get(url, headers=headers)
    print('code={0},{1}'.format(response.status_code, response.text))
    return json.loads(response.text)


def video_save(id_course, id_lesson, lesson_child):
    response = requests.get(lesson_child['url'])
    dir = os.path.abspath('{0}/{1}'.format(path_video_jiker, id_course))
    if os.path.exists(dir) is False:
        directory = Path(dir)
        Path.mkdir(directory, parents=True)
    videoName = '{0}_{1}_{2}.mp4'.format(id_lesson, lesson_child['id'], lesson_child['name']).replace(' ', '')
    file = '{0}/{1}'.format(dir, videoName)
    if os.path.exists(file) is True:
        print('{0}文件已存在'.format(videoName))
        return
    with open(file, 'wb') as f:
        f.write(response.content)
        f.flush()
        print('{0} success'.format(videoName))


# 单个课程详情
def request_detail(id):
    response_detail = request_http(url_data_detail.format(id))
    id_course = '{0}.{1}'.format(response_detail['data']['course']['id'], response_detail['data']['course']['name'])
    print('---id_course={}'.format(id_course))
    list_lesson = response_detail['data']['course']['content']
    for lesson in list_lesson:
        list_lesson_child = lesson['children']
        for lesson_child in list_lesson_child:
            video_save(id_course, lesson['id'], lesson_child)


# 课程列表
print('start')
for page in range(12):
    loadData_response = request_http(url_data_list.format(page))
    data_list = loadData_response['data']['list']
    for item in data_list:
        if not (item['is_vip']):
            request_detail(item['id'])
print('end')
