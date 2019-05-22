"""
    面向对象：考虑问题，从对象的角度出发．
    类：模板　　抽象
    对象：具体　
"""


class Wife:
    """
        老婆
    """

    # 1.数据成员 姓名　年龄　性别　．．．
    def __init__(self, name, age, sex):
        # self "自己"，调用当前方法的对象
        print(id(self))
        self.name = name
        self.age = age
        self.sex = sex

    # 2.方法成员 做饭　．．．
    def cooking(self):
        print(id(self))
        print(self.name + "做饭")


# 创建对象(实例化)
# 调用 __init__(self,name,age,sex) 方法
w01 = Wife("丽丽", 21, "女")
print(id(w01))
# 调用对象的方法 w01 将自身传入方法
w01.cooking()


w02 = Wife("芳芳", 22, "男")
w02.cooking()
print(id(w02))

# 在内存中，方法只有一份．而对象有多份．
