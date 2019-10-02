# 根据年份判断生肖

zodiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"
# 切片操作符
print(zodiac[0:4])
print(zodiac[-1])

year = 2018
print(year % 12)
print(zodiac[year % 12])
# 成员关系操作符
print('狗' not in zodiac)
# 字符串连接操作符
print(zodiac + zodiac)
# 字符串重复操作符
print(zodiac * 2)

# 元组
a = (1, 3, 5, 7, 9)
# 取出a中小于8的元素
print(list(filter(lambda x: x < 8, a)))
# 取出a中小于8的元素个数
print(len(list(filter(lambda x:x<8,a))))

# 根据日期判断星座
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_day = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
              (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
# 元组比较大小
# print(zodiac_day[0]>zodiac_day[1])
(month, day) = (4,30)
zodiac_day = filter(lambda x: x <= (month, day), zodiac_day)
# print(list(zodiac_day))
zodiac_len = len(list(zodiac_day))
print(zodiac_name[zodiac_len])

# 列表
a_list = ['a', 'b', 'c']
a_list.append('d')
a_list.append(True)
print(a_list)
a_list.remove('c')
print(a_list)



