# 根据年份判断生肖

zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
# year = int(input('请输入年份'))
# print(zodiac[year%12])

# for 循环
for zc in zodiac:
    print(zc)

for zc in range(1,13):
    print(zc)

for year in range(2000,2019):
    print('%s年的生肖是 %s' %(year,zodiac[year % 12]))

age = 20
while True:
    if age == 25:
        print('age=', age)
        break
    else:
        print('age is %s not 25' %(age))
    age = age + 1


# 根据日期判断星座
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_day = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
              (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
(month, day) = (12,30)

for num in range(len(zodiac_day)):
    if zodiac_day[num] >= (month,day):
        print(zodiac_name[num])
        break
    elif month == 12 and day > 23:
        print(zodiac_name[0])
        break

# zodiac_day = filter(lambda x: x <= (month, day), zodiac_day)
# zodiac_len = len(list(zodiac_day))
# print(zodiac_name[zodiac_len])
