temp={}
print(type(temp))

temp=dict()
print(type(temp))
print('=======1')

temp = {'中':'100',
        '左':'200'}
print(temp['中'])
print('=======2')

words =['中','左']
location = [100,200]
print(location[words.index('中')])
print('=======3')

# 拉锁函数
temp2 = [['中','左'],[100,200]]
print(type(temp2))
print('=======4')

temp3 = (['中','左'],[100,200])
print(type(temp3))
print('=======5')

temp4 = (words,)
print(type(temp4))
print('=======6')

print(list(zip(temp)))
print(list(zip(temp2)))
print(list(zip(words,location)))
print('=======7')

# 生成字典
students = ['zhao','qian','sun','li']
dict_students = dict.fromkeys(students,100)
print(dict_students)
print('=======8')

# 访问字典中的值
print(dict_students['zhao'])
print(dict_students.get('zhou',200))
print('=======9')

print(dict_students.values())
print(dict_students.items())


