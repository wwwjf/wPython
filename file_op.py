#写文件
file1 = open('file_op.txt','w')
file1.write('zhangsan\nlisi')
file1.close()

#读文件
file2 = open('file_op.txt')
print('file_op.txt内容：'+file2.read())
#file2.close()

#增加文件内容
file3 = open("file_op.txt",'a')
file3.write("\n增加文件内容---------")
file3.close()
print(file2.read())
file2.close()

file4 = open('file_op.txt')
print('当前位置%s'%file4.tell())
print('第一行内容：'+file4.readline())
print('当前位置%s'%file4.tell())
file4.close()