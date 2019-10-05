import os
from pathlib import Path
from dotenv import load_dotenv


print(os.path.abspath('.'))
print(os.path.exists('/Users/wengjianfeng/github'))
print(os.path.isdir('/Users/wengjianfeng/github'))

print('-------------')
path = Path('.')
print(path.resolve())
print(path.is_dir())
print(path.is_file())
print('-------------创建文件夹')
# directory = Path('temp/a/b/c')
# Path.mkdir(directory, parents=True)


load_dotenv()
password = os.getenv('PASSWORD')
print(f'password:===={password}')
