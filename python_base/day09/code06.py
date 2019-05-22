"""
    使用属性封装变量
"""

# 练习：修改Enemy类，使用属性封装变量
class Wife:
    def __init__(self, name="", age=0):
        self.name = name  # 调用 @name.setter 修饰的方法
        self.age = age  # 调用 @age.setter 修饰的方法

    @property  # 拦截读取变量的操作
    def name(self):  # get_name()
        return self.__name

    @name.setter  # 拦截写入变量的操作
    def name(self, value):  # set_name()
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 20 <= value <= 30:
            self.__age = value
        else:
            self.__age = 0
            print("我不要")


w01 = Wife("铁锤", 86)
print(w01.name)
print(w01.age)
