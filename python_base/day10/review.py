"""
    day09 复习
    1. 实例成员
    2. 类成员
    3. 静态方法
    4. 属性
"""


# 1.实例成员:对象的成员(创建对象,就会开辟空间,存储的数据)
#   作用:表示对象的信息,与对象的行为.

class A:
    def __init__(self, 参数):
        self.实例变量 = 参数

    def 实例方法名称(self):
        print(self.实例变量)


a01 = A(10)
print(a01.实例变量)
a01.实例方法名称()  # 自动传递对象地址


# 2.类成员:属于类级别的成员
#   表示所有对象共享的成员
class B:
    # 无论创建多少对象,类变量只有一份,被所有对象所共享.
    类变量 = 10

    # 类方法:操作类变量
    # 因为没有对象地址,所以不能操作实例成员.
    @classmethod
    def 类方法名称(cls):
        print(cls.类变量)


print(B.类变量)
B.类方法名称()  # 自动传递类名


# 函数
# def fun01():
#     print("函数执行啦")
#
#
# fun01()


class C:
    # 3.静态方法
    @staticmethod
    def fun01():
        print("方法执行啦")


C.fun01()


# 4. 属性
class D:
    def __init__(self,name):
        # 写入操作
        self.name = name

    # 拦截读取操作
    # 本质:创建property对象,name 存储对象地址.
    # 注意: 创建对象时,会指定读取方法
    # 相当于: name  = property(读取方法,None)
    @property
    def name(self):
        # 逻辑判断
        return self.__name

    # 拦截写入操作
    @name.setter  # 本质:name.setter(写入方法)
    def name(self,value):
        # 逻辑判断
        self.__name = value


d01 = D("张三")
d01.name = "老三"  # 写入操作
print(d01.name) # 读取操作

# 只读属性
class E:
    def __init__(self, a):
        self.__a = a

    # 拦截读取操作
    @property
    def a(self):
        # 逻辑判断
        return self.__a


e01 = E(100)
# e01.a = 10 # 错误
print(e01.a)


# 属性本质
class F:
    def __init__(self,a):
        # 写入操作
        self.a = a

    def get_a(self):
        print("读取变量喽")
        return self.__a

    def set_a(self, value):
        print("设置变量喽")
        self.__a = value

    # 拦截对变量a的读写操作
    # 创建property对象,a存储的是对象地址.
    # 注意:创建对象时,需要传递读写方法
    a = property(get_a,set_a)


f01 = F(10)
f01.a = 200 # 写入
print(f01.a) # 读取

# 只写属性
class G:
    def __init__(self,a):
        # 写入操作
        self.a = a

    def set_a(self, value):
        print("设置变量喽")
        self.__a = value

    # 拦截对变量a的写入操作
    a = property(None,set_a)


g01 = G(100)
g01.a = 200
# print(g01.a) # 错误
print(g01._G__a)



