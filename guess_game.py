import random

# 我出 石头，电脑出 剪刀   结果：我赢



print('------人机猜拳小游戏-----')
print('开始')
while(True):
    you = int(input('请出拳：(石头-1，剪刀-2，布-3)'))
    computer = random.randint(1, 3)
    if ((you == 1 and computer == 2) or
        (you == 2 and computer == 3) or
            (you == 3 and computer == 1)):
        print('你赢了')
    elif you == computer:
        print('平局')
    else:
        print('你输了')
