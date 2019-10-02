import itchat
itchat.login()
friends = itchat.get_friends(update=True)[0:]

male = female = other = 0
# friend[0]是自己的信息 从friends[1]开始
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

# 计算朋友总数
total = len(friends[1:])
# 打印出好友性别比例
print("男性好友：%2f%%" % (float(male)/total*100) + "\n" +
      "女性好友：%2f%%" % (float(female)/total*100) + "\n" +
      "不明性别好友：%2f%%" % (float(other)/total*100) + "\n" +
      "好友总数：%2d" % total)
