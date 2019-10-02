import matplotlib.pyplot as plt
import numpy as np

# 绘制简单曲线
# plt.plot([1, 3, 5], [2, 4, 5])
# plt.show()

# x = np.linspace(-np.pi * 2, np.pi * 2, 100)  # x轴的定义域-2pi~2pi 中间间隔100个元素
# plt.figure(2, dpi=50)  # 创建图表2 精度50
# for i in range(1, 5):  # 创建四条曲线
#     plt.plot(x, np.sin(x / i))
# plt.show()

# plt.figure(1, dpi=100)
# data = [1, 1, 1, 2, 2, 2, 3, 5, 6, 7, 8, 9]
# plt.hist(data)  # 直方图 统计数据出现的次数
# plt.show()

# x = np.arange(1, 10)
# y = x
# fig = plt.figure()
# plt.scatter(x, y, c='r', marker='D')  # c='r' 散点的颜色红色， marker='o' 散点形状为圆形,D为正方形
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# iris = pd.read_csv('./iris_training.csv')
# print(iris.head())
# # 绘制散点图
# iris.plot(kind='scatter', x='120', y='4')
# plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import warnings

warnings.filterwarnings('ignore')

iris = pd.read_csv('./iris_training.csv')
sns.set(style='white', color_codes=True)

# FacetGrid一般绘图函数
# hue 彩色显示分类0/1/2
# plt.scatter 绘制散点图
# add_legend() 显示分类的描述信息
# sns.FacetGrid(iris, hue='virginica', size=5).map(plt.scatter, "120", "4").add_legend()
sns.FacetGrid(iris, hue='virginica', size=5).map(plt.scatter, 'setosa', 'versicolor').add_legend()
plt.show()
