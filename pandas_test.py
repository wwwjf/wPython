from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from numpy import nan as NA

obj = Series([4, 5, 6, -7])
print(obj)
print(obj.index)
print(obj.values)
print('-----------------')

obj2 = Series([4, 5, 6, -7], index=['a', 'b', 'c', 'd'])
print(obj2)
print(obj2['c'])
obj2['c'] = 60
print(obj2['c'])
print(obj2)
print('d' in obj2)
print('-----------------')

sdata = {'beijing': 35000, 'shanghai': 71000, 'guangzhou': 16000, 'shenzhen': 5000}
obj3 = Series(sdata)
print(obj3)
obj3.index = ['bj', 'sh', 'gz', 'sz']
print(obj3)
print('-----------------')

data = {'city': ['shanghai', 'guangdong', 'shenzhen', 'xiamen', 'beijing'],
        'year': [2016, 2015, 2018, 2017, 2019],
        'pop': [1.5, 1.7, 1.6, 1.8, 1.9]}
frame = DataFrame(data)
print(frame)
frame2 = DataFrame(data, columns=['year', 'city', 'pop'])
print(frame2)

print(frame2['city'])
print(frame2.city)

frame2['newCol'] = [100, 101, 102, 103, 104]
frame2['cap'] = frame2.city == 'beijing'
print(frame2)

pop = {'beijing': {2008: 1.5, 2009: 2}, 'beijing': {2008: 1.5, 2009: 2}}
print(pop)
frame3 = DataFrame(pop)
print(frame3.T)

obj4 = Series([1.2, 2.2, 4.2, 5], index=['a', 'c', 'e', 'f'])

obj5 = obj4.reindex(['a', 'b', 'c', 'd'], fill_value=0)
print(obj5)

obj6 = Series(['blue', 'yellow', 'red'], index=[0, 2, 4])

print(obj6.reindex(range(6), method='bfill'))

data = Series([1, NA, 2])
print(data.dropna())

data2 = DataFrame([[1., 6.5, 4], [1., NA, NA], [NA, NA, NA]])
data2[4] = NA
print(data2)  # 有na值都不输出
print('------------')

print(data2.dropna(axis=1, how='all'))
print('------------')

data3 = data2.fillna(0)  # 空值替换为0
print(data3)
print('------------')

data3 = data2.fillna(0, inplace=False)  # 空值替换为0
print(data3)
print('------------')

# 层次化索引
data4 = Series(np.random.randn(10),
               index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                      [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])

print(data4)
print('------------')

print(data4['b'])
print('------------')
print(data4.unstack())  # 一维转换为二维
print('------------')
print(data4.unstack().stack())  # 二维数据转换为一维数据
