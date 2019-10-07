import requests

remortip = input("要扫描的ip：")

url_toolcc = "http://tool.cc/port/check_port_status.php"


def get_params_toolcc(ip, port):
    return "by=2&remoteip={0}&port={1}&lang=cn".format(ip, port)


for i in range(20):
    response = requests.get(f'{url_toolcc}?{get_params_toolcc(remortip, 2440 + i)}')
    print(response.text)
