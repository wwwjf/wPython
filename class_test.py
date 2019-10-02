class Player():  # 定义一个类
    def __init__(self, name, hp):
        self.__name = name
        self.hp = hp

    def print_role(self):  # 定义一个方法
        print('%s: %s' % (self.__name, self.hp))

    def updateName(self, newName):
        self.__name = newName


class Monster():
    '定义怪物类'

    # pass  # 忽略
    def __init__(self, hp=100):
        self.hp = hp

    def run(self):
        print('移动到某个位置')

    def whoami(self):
        print('我是怪物类')


class Animals(Monster):
    '普通怪物'

    # pass
    def __init__(self, hp=10):
        super().__init__(hp)


class Boss(Monster):
    'Boss类怪物'

    def __init__(self, hp=1000):
        super().__init__(hp)

    def whoami(self):  # 继承 重载
        print('我是boss 我怕谁')


a1 = Monster(200)
print('生命值初始值：%s' % a1.hp)
print(a1.run())
a2 = Animals(100)
print(a2.hp)
print(a2.run())

a3 = Boss(8000)
print('boss生命初始值：%s' % a3.hp)
a3.whoami()

# user1 = Player('tom', 100)  # 类的实例化
# user1.updateName('jane')
# user1.print_role()
#
# user2 = Player('jerry', 200)
# user2.updateName('jack')
# user2.print_role()
