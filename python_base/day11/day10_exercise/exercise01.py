# 1. 使用面向对象思想,写出下列场景:
#     玩家(攻击力)攻击敌人,敌人受伤(血量)后掉血,还可能死亡(播放动画).
#     敌人(攻击力)攻击力攻击玩家,玩家(血量)受伤后碎屏,还可能死亡(游戏结束).
#     程序调试,画出内存图.

class Player:
    """
        玩家类
    """
    def __init__(self,hp,atk):
        self.atk = atk
        self.hp = hp

    def attack(self,enemy):
        print("打死你")
        # 调用敌人受伤方法(敌人负责定义受伤逻辑)
        enemy.damage(self.atk)

    def damage(self,value):
        self.hp -= value
        print("玩家受伤啦,屏幕碎啦")
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print("玩家死亡,游戏结束")


class Enemy:
    def __init__(self,hp,atk):
        self.hp = hp
        self.atk = atk

    def damage(self,value):
        self.hp -= value
        print("受伤啦")
        if self.hp <= 0:
            self.__death()

    def attack(self,player):
        print("打死你")
        player.damage(self.atk)

    def __death(self):
        print("死啦,播放动画")


p01 = Player(100,50)
e01 = Enemy(60,10)
# 玩家打敌人
p01.attack(e01)
# p01.attack(e01)
e01.attack(p01)





