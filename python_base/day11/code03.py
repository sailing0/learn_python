"""
    继承 -- 设计思想
    面向对象设计原则
    练习:exercise01.py
    1. 开闭原则
       开放     关闭
       对扩展   对修改
       允许增加新功能   不允许改变(增加/删除/修改)以前的代码

    2. 依赖倒置(抽象)
        使用抽象(父类),而不使用具体(子类).
"""
# 老张开车去东北
# 变化:飞机
#      火车
#      汽车
#      .......

class Person:
    def __init__(self, name):
        self.name = name

    # def go_to(self, str_type, str_pos):
    #     if str_type == "汽车":
    #         Car().run(str_pos)
    #     elif str_type =="飞机":
    #         Airplane().fly(str_pos)
    #     # elif xxxxx:

    def go_to(self, vehicle, str_pos):
        """
            写代码期间:
                使用的是交通工具的,而不是汽车,飞机等
                所以无需判断具体类型
            运行期间:
                传递具体的对象(汽车,飞机)
        :param vehicle:
        :param str_pos:
        :return:
        """

        vehicle.transport(str_pos)


# class Car:
#     def run(self, str_pos):
#         print("行驶到", str_pos)
#
#
# class Airplane:
#     def fly(self, str_pos):
#         print("飞到", str_pos)

class Vehicle:
    """
        交通工具
    """
    def transport(self, str_pos):
        # 人为创造一个错误()
        raise NotImplementedError()
        # print("儿子们,必须有这个方法啊")

class Car(Vehicle):
    def transport(self, str_pos):
        # super().transport()
        print("行驶到", str_pos)


class Airplane(Vehicle):
    def transport(self, str_pos):
        print("飞到", str_pos)

# ....
p01 = Person("老张")
# p01.go_to("汽车", "东北")
p01.go_to(Car(),"东北")





