# 端口扫描
import requests

host = input("要扫描的IP:")

url_chinaz = "http://tool.chinaz.com/iframe.ashx"
encode_value_chinaz = "ak5OGl2j2~KWSocmj16ZlWAyMNTxODK9"
params_chinaz = {
    "host": host,
    "port": 2445,
    "encode": encode_value_chinaz
}


def get_params_chinaz(value):
    return 2460 + value


for i in range(2):
    port = get_params_chinaz(i)
    response = requests.post(f'{url_chinaz}?t=port&callback=jQuery123_564\
    ', params_chinaz)
    print(f'{response.status_code},i={i},port={port}')
    print(response.text)
