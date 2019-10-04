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
