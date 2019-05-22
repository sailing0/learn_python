"""
    day11 复习
    继承

"""


class 爸爸:
    def __init__(self, 数据):
        self.爸爸数据1 = 数据

    def 方法1(self):
        print("方法1")


class 儿子(爸爸):
    # 子类没有构造函数,则自动调用父类构造函数
    # 子类有构造函数,不再自动调用父类构造函数
    def __init__(self, 爸爸数据, 儿子数据):
        super().__init__(爸爸数据)
        self.子儿子数据 = 儿子数据

    def 方法2(self):
        print("方法2")


c01 = 儿子(10, 20)
c01.方法1()
c01.方法2()
# 判断对象与类型
print(isinstance(c01, 爸爸))
# 判断类型与类型
print(issubclass(儿子, 爸爸))

print(c01.爸爸数据1)
