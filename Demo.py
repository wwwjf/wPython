# -*- coding:utf-8 -*-
i = 1
j = 2
print('i+j=', i + j)
print('-------------------')

# name=input("input your name:")
# print("hello "+name)

print('-------------------')

print(1024 * 768)

print('-------------------')

a = 10
if a > 0:
    print("a>0")
else:
    print("a<0")
    print("i+j=", i + j)
print("-------------------")

print("I'm ok")

print('Im "ok ')

print('I\'m \"ok\"')

print("-------------------")

# 转义字符
print('hello\npython')

print('hello\t python')

# r‘内部不转义
print(r'i\tm ok ')
print('i\tm ok ')

# 多行
print('''line1
ine2
line3''')
# r' 多行不转义
print(r'''hello,\n
world''')

print(True & False)
print('3 > 2 =', 3 > 2)

x = False
# x = 123
print('x=', x)

x = 'a'
x += 'b'
print('x=', x)

X = None
print('X=', X)

y = 10 / 3
print('y=', y)

z = 10 // 3
print('z=', z)

Z = 10 % 3
print('Z=', Z)

print(r'输出十六进制\u4e2d\u6587对应的中文：', '\u4e2d\u6587')

y = '中文'.encode("UTF-8")
print(y)
x = b'\xe4\xb8\xad\xe6\x96\x87'.decode("UTF-8")
print(x)

Z = b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
print(Z)

x = len('中'.encode('utf-8'))
print(x)
x = len("a")
print(x)
x = len('中')
print(x)
x = len(b'\xe4\xb8\xad')
print(x)

x = 'hello,%s %d' % ('world', 3)
print(x)

print('%2d,%02d' % (3, 3))
print('%.2f' % 3.1415926)
print('%s' % True)
print('%d%%' % 50)
print('hello,{0},你的成绩提升了{1}分'.format('小明', 30))
print('hello,{0},你的成绩提升了{1:.2f}%'.format('小明', 30.123))

x = ['jack', 'pony', 'jacky']

print(x)
print(x[0])
x[0] = 'pony'
print(x)

import time

print(time.time())

type('123')

y = 'abcd'
x1, x2, x3, x4 = y
print('x1=', x1, ',x2 =', x2)

y1 = ['y11', 'y12', 'y13', 'y14']
y2 = ['y21', 'y22', 'y23', 'y24']
y3 = ['y31', 'y32', 'y33', 'y24']
y4 = ['y41', 'y42', 'y43', 'y44']

z = [y1, y2, y3, y4]
print(z[1][1])
print(z[-0][1])

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])
y1 = ('y111', 'y112', 'y113', 'y114')
y2 = ('y221', 'y222', 'y223', 'y224')
z = (y1, y2)
print(z[0][0])
age = 20
if age > 18:
    print("成年")
elif age > 12:
    print("青少年")
else:
    print("幼儿")

for y in y1:
    print(y)
sum = 0
for sum in range(1000):
    sum += sum
print(sum)
# 字典
a = {'food': 'rice', 'price': 4.5, 'weight': 5}
print('food name ', a["food"])
print('food price ', a['price'])
b = ('b1', 'b2', 'b3', 'b4')
c = ('c1', 'c2', 'c3', 'c4', 'c5', 'c6')
a = {'ab': b, 'ac': c}
print('输出a字典中b的内容', a['ab'])
print('输出a字典中b 第一个位置的内容', a['ab'][0])

# name = raw_input('你的名字：')  # python2
name = input('你的名字：')  # python3
'''多行注释
多行注释....'''
print('hello,', name)
