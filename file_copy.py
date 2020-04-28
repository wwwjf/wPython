# 复制文件夹和子文件夹下文件格式为.java的文件，
# 并在相同文件夹目录下创建同名的文件，文件格式为.txt
# (如 复制D:/test/test.java，创建D:/test/test.txt)，
# 测试文件夹： https://share.weiyun.com/56cpZSH


import os
rootPath = '/users/code/androidStudioProjects/epay-app-android/'
sourceFile = open('{0}{1}'.format(rootPath, 'local.properties'))
content = sourceFile.read()
# print(content)
dir = os.listdir(rootPath)
# print(dir)

# nowPath = os.path.abspath(rootPath)
# print(nowPath)
# destFile = open('{0}/{1}'.format(nowPath,'local.txt'),'w')
# destFile.write(content)
# destFile.close()

# for dirPath,dirNames,fileNames in os.walk(rootPath):
#     for fileName in fileNames:
#         print(dirPath)

flag = os.path.isdir(rootPath)
print(flag)
