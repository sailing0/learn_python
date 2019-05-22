# 1. 定义父类:武器,数据:攻击力,行为:购买(所有子类都一样).攻击(不知道怎么攻击)
#    定义子类:枪,数据:射速,行为:攻击
#    定义子类:手雷,数据:爆炸范围,行为:攻击
#    创建相应对象,调用相应方法.
#    画出内存图

class Weapon:
    """
        武器
    """
    def __init__(self,atk):
        self.atk = atk

    def buy(self):
        print("购买武器")

    def attack(self):
        # 子类如果没有当前方法,就会报错
        raise  NotImplementedError()


class Gun(Weapon):
    """
        枪
    """
    def __init__(self,atk,speed):
        super().__init__(atk)
        self.att_speed = speed

    def attack(self):
        print("开枪啦")

class Grenade(Weapon):
    """
        手雷
    """

    def __init__(self, atk, range):
        super().__init__(atk)
        self.explode_range = range

    def attack(self):
        print("爆炸啦")

g01 = Gun(10,0.1)
g01.buy()
g01.attack()# 调用的是子,所以不构成多态

grenade01 = Grenade(50,10)
grenade01.buy()
grenade01.attack()


def use(weapon):
    # weapon.buy()# 因为执行的是父,所以不构成多态.
    weapon.attack() # 1. 调用父类

use(g01)# 2.执行子类






