"""
    练习：方法封装变量
"""
class Enemy:
    def __init__(self,name,atk,speed,hp):
        self.set_name(name)
        self.set_atk(atk)
        self.set_atk_speed(speed)
        self.set_hp(hp)

    def get_name(self):
        return self.__name

    def set_name(self,value):
        self.__name = value

    def get_atk(self):
        return self.__atk

    def set_atk(self, value):
        self.__atk = value

    def get_atk_speed(self):
        return self.__atk_speed

    def set_atk_speed(self, value):
        if 0 <= value <= 10:
            self.__atk_speed = value
        else:
            self.__atk_speed = 0
            print("速度不再范围内，赋值失败")

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        if 0 <= value <= 100:
            self.__hp = value
        else:
            self.__hp = 0
            print("血量不再范围内，赋值失败")


e01 = Enemy("zs",200,50,200)
print(e01.get_name(),e01.get_hp(),e01.get_atk_speed())



