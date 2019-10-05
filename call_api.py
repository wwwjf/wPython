import requests
import json

image_path="./temp/image/Snipaste.png"
qrcode_path = "./temp/qrcode/qrcode.png"
image_data = open(image_path,"rb").read()

api_url = "http://qr.topscan.com/api.php"

params = {"text":"1234",
          "bg":"ffffff",
          "fg":"ff0000"}

response = requests.get(f'{api_url}',params)
print(f'code:{response.status_code}')
if response.status_code==200:
    print(f'文件大小：{len(response.content)}')
    qrcode_file = open(qrcode_path, "wb")
    qrcode_file.write(response.content)
    qrcode_file.close()
    print(response.content)

print("---------------------------")
# print(response.content.decode(encoding="utf-8"))


weather_url = "http://wthrcdn.etouch.cn/weather_mini?citykey=101010100"

response = requests.get(weather_url)
if response.status_code == 200:
    result = response.json()
    print(result)
    jsonResult = json.dumps(result)
    print(result["data"]['yesterday']['date'])

