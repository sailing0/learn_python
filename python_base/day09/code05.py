"""
    封装数据优势：
     １．符合人类思考方式
     ２．将数据与对数据的操作封装起来。

     使用方法封装变量
"""


class Wife01:
    def __init__(self, name, age):
        self.name = name
        # 缺点：缺乏对象数据的封装，外界可以随意赋值．
        self.age = age


w01 = Wife01("芳芳", 26)
w02 = Wife01("铁锤", 86)
w02.age = 87
# print(w02.age)

# 注意：通过两个方法，读写私有变量．
# 练习：定义敌人类(姓名，攻击力，攻击速度(０－１０)，血量(０－－１００))
class Wife02:
    def __init__(self, name = "", age = 0):
        self.set_name(name)
        # 私有成员：障眼法(解释器会改变双下划线开头的变量名)
        # self.__age = age
        self.set_age(age)

    def get_name(self):
        return self.__name

    def set_name(self,value):
        self.__name = value

    def get_age(self):
        return self.__age

    def set_age(self,value):
        if 20 <= value <= 30:
            self.__age = value
        else:
            print("我不要")

w01 = Wife02("铁锤",86)
# 找不到双下划线开头的数据
# print(w01.__age)
# 通过下划线　＋　类名 可以访问双下划线开头的数据
# print(w01._Wife02__age)
w01.set_age(50)
print(w01.get_age())
print(w01.__dict__)






