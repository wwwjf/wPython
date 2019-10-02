# 输出 1到99中一半的数
# L = []
# n = 1
# while n <= 99:
#     L.append(n)
#     n = n + 2
#
# print(L)


# L = ['MIKE', 'Jane', 'Lucy', 'Kate', 'Lucky']
# for i in range(len(L)):
#     print(L[i])  # 输出全部
#
# # 输出部分
# L2 = L[0:3]  # 切片
# for i in range(len(L2)):
#     print(L[i])
#
# L3 = list(range(50))
# print(L3[:10])

# 用切片去除字符串后的空格
def trim(s):

    while s != '' and s[0] == ' ':
        s = s[1:]
        print(s)
    while s != '' and s[-1] == ' ':
        s = s[0:-1]
    return s


# test
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
