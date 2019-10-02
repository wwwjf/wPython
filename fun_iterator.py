# 迭代
from collections import Iterable

# 字典
d = {'a': 1, 'b': 2, 'c': 3, 'b': 4}
# print(dict)
for i in d:
    print(i + ':', d[i])
# list
l = ['a', 'c', 'f', 'b', 'd', 'b']
for i in l:
    print(i)

# tuple
t = ('a', 'c', 'f', 'b', 'd', 'b')
print(t)
# set
s = {'1', '2', '2', '3'}
print(s)

print(isinstance(d, Iterable))  # 是否可迭代
print(isinstance(l, Iterable))  # 是否可迭代
print(isinstance(s, Iterable))  # 是否可迭代

s2 = [(1, 1), (2, 4), (3, 9)]
for key, value in enumerate(s):
    print(key, value)
for key, value in [(100, 1), (22, 4), (3, 9)]:
    print(key, value)


# 找到list中的最小值和最大值
def find_min_max(list):
    if not list:
        return None, None
    min = max = list[0]
    for i in list:
        if min > i:
            min = i
        if max < i:
            max = i
    return min, max


# 测试
if find_min_max([]) != (None, None):
    print('测试失败!')
elif find_min_max([7]) != (7, 7):
    print('测试失败!')
elif find_min_max([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
