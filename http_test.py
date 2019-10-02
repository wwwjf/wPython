# -*- encoding: utf-8 -*-
from http import client
from urllib import request, parse


class HTTP:
    def __init__(self, url, gwid=""):
        self.url = url
        self.GWID = gwid

    def GET_info(self):
        header = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-cn,zh;q=0.8",
            "Connection": "keep-alive",
        }
        conn = client.HTTPConnection(self.url)
        allurl = "/router/" + self.GWID + "/wans"
        print(allurl)
        conn.request(method="GET", url=allurl, headers=header)
        rl = conn.getresponse()
        data = rl.read()
        host_info = data.decode("utf-8")
        print(host_info)

    def POST_info(self):
        header = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-cn,zh;q=0.8",
            "Connection": "keep-alive",
        }
        bodydata = '''{
        "state":"up",
        "event":"reboot",
        "strategy":"week",
        "date":"1",
        "time":"15:00",
        "comment":""
        }'''

        print(bodydata)
        conn = client.HTTPConnection(self.url)
        allurl = "/router/" + self.GWID + "/power/schedule"
        print(allurl)
        conn.request(method="POST", url=allurl, body=bodydata, headers=header)
        rl = conn.getresponse()
        data = rl.read()
        host_info = data.decode("utf-8")
        print(host_info)

    def PUT_info(self):
        header = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-cn,zh;q=0.8",
            "Connection": "keep-alive",
        }
        bodydata = '''{
        "state":"up",
        "event":"reboot",
        "strategy":"week",
        "date":"2",
        "time":"15:00",
        "comment":""
        }'''
        print(bodydata)
        conn = client.HTTPConnection(self.url)
        allurl = "/router/" + self.GWID + "/power/schedule/1"
        print(allurl)
        conn.request(method="PUT", url=allurl, body=bodydata, headers=header)
        rl = conn.getresponse()
        data = rl.read()
        host_info = data.decode("utf-8")
        print(host_info)

    def DELETE_info(self):
        header = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-cn,zh;q=0.8",
            "Connection": "keep-alive",
        }
        conn = client.HTTPConnection(self.url)
        allurl = "/router/" + self.GWID + "/power/schedule/2"
        print(allurl)
        conn.request(method="DELETE", url=allurl, headers=header)
        rl = conn.getresponse()
        data = rl.read()
        host_info = data.decode("utf-8")
        print(host_info)


if __name__ == "__main__":
    url = "192.168.2.116:2049"
    gwid = "b28b8b51399fcfa5c0e96164e20d38c5"
    hp = HTTP(url, gwid)
    hp.PUT_info()
