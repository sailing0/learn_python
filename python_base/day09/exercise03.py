"""
    练习：属性封装变量
"""


class Enemy:
    def __init__(self, name, atk, speed, hp):
        self.name = name
        self.atk = atk
        self.speed = speed
        self.hp = hp

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp= value


e01 = Enemy("zs", 200, 50, 200)
print(e01.name, e01.hp, e01.speed)
