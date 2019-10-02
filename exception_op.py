try:
    a = open("file_op.txt")
    print('文件内容', a.read())
    print('文件读取结束\n')
except Exception as e:
    print(e)
finally:
    a.close()
    print('finally关闭文件')
