# 1、打印输入的可变长度参数内容
# def printParam(*param):
#     for index in range(len(param)):
#         print(param[index])
#
#
# printParam('111111', '2222', '23333')


# 2、生成器
# def frange(start, end, step):
#     x = start
#     while x <= end:
#         yield x
#         x += step
#
#
# for i in frange(0, 10, 0.5):
#     print(i)


# 3、闭包(内部函数应用外部变量
# def func():
#     a = 1
#     b = 2
#     return a + b
#
#
# def sum(a):
#     def add(b):
#         return a + b
#
#     return add
#
#
# num1 = func()
# num2 = sum(2)
# # 类型
# print(type(num1))
# print(type(num2))
# # 值
# print(num2(1))
#
#
# # 计数器
# def counter(first=0):
#     cnt = [first]
#
#     def add_one():
#         cnt[0] += 1
#         return cnt[0]
#
#     return add_one
#
#
# num10 = counter(10)
# print(num10())


# 4、闭包使用 ax+b=y线性函数
# def a_line(a, b):
#     def arg_y(x):
#         return a * x + b
#
#     return arg_y
#
#
# line_1 = a_line(2, 3)
# line_2 = a_line(5, 5)
# print(line_1(1))
# print(line_1(10))
# print(line_2(1))
# print(line_2(10))

# 5、装饰器(闭包的运用
# import time
#
#
# # 普通函数写法
# # def i_can_sleep():
# #     time.sleep(3)
# # start_time = time.time()
# # i_can_sleep()
# # stop_time = time.time()
# # print('程序运行时间 %s' % (stop_time - start_time))
#
#
# # 装饰器写法
# def timmer(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print('程序运行时间 %s' % (stop_time - start_time))
#
#     return wrapper
#
#
# @timmer
# def i_can_sleep():
#     time.sleep(3)
#
#
# i_can_sleep()


# 6、装饰器的使用
# def new_tips(args):
#     def tips(func):
#         def nei(a, b):
#             print('start %s %s' % (args,func.__name__))
#             func(a, b)
#             print('stop')
#
#         return nei
#
#     return tips
#
#
# @new_tips('add_module')
# def add_modu(a, b):
#     print(a + b)
#
#
# @new_tips('sub_module')
# def sub(a, b):
#     print(a - b)
#
#
# print(add_modu(4, 5))
# print(sub(5, 1))

# 7、上下文管理器
# 第一种写法 普通写法
# fd = open('file_op.txt')
# try:
#     for line in fd:
#         print(line)
#
# finally:
#     fd.close()
# # 第二种写法 上下文管理器
# with open('fun_op.txt') as f:
#     for line in f:
#         print(line)

# # 调用hex函数输出16进制数
# n1 = 1000
# n2 = 255
# print(hex(n1))
# print(hex(n2))

# # 自定义函数
# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
#
#
# print(my_abs(-9))


# # 返回 两个值
# def move(x, y, step, angel=0):
#     nx = x + step * math.cos(angel)
#     ny = y - step * math.sin(angel)
#     return nx, ny
#
#
# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)


# # 默认平方值
# def power_(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
#
# print(power_(2, 3))
# print(power_(3))


# # 计算一组数的平方值
# def calsqrt(nums):
#     sum = 0
#     for n in nums:
#         sum = sum + n * n
#
#     return sum
#
#
# sum = calsqrt([1, 2, 3])
# print(sum)

# # 计算一组数的平方值 可变参数长度
# def calsqrt2(*nums):
#     sum = 0
#     for n in nums:
#         sum = sum + n * n
#
#     return sum
#
#
# num1 = (2, 3, 4)
# num2 = (3, 4, 5, 6)
# num3 = [3, 2]
# print(calsqrt2(*num1))

import sys
sys.setrecursionlimit(10000)
def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


# 深度有限制
print(fact(1000))
