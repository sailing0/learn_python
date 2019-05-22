# 练习:手雷爆炸了,可能伤害敌人,玩家.还有可能伤害未知事物(鸭子,树,房子).
# 要求:如果增加了新的事物,手雷代码不变. 17:15

class Grenade:
    """
        手雷
    """

    def __init__(self, atk):
        self.atk = atk

    def explode(self, *args):
        """
            爆炸
        :return:
        """
        for item in args:
            if not isinstance(item, Damageable):
                print("类型不兼容")
                return
            item.damage(self.atk)


class Damageable:
    """
        可以受伤
    """

    def __init__(self, hp):
        self.hp = hp

    def damage(self, value):
        # 约束子类必须具有当前方法
        # raise NotImplementedError()
        self.hp -= value


class Player(Damageable):
    def damage(self, value=0):
        # self.hp -= value
        super().damage(value)
        print("碎屏")


class Enemy(Damageable):
    def damage(self, value):
        # self.hp -= value
        super().damage(value)
        print("播放动画")


g01 = Grenade(10)
p02 = Player(100)
e03 = Enemy(50)
g01.explode(p02, e03)
