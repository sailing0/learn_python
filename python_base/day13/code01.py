"""
    多继承
"""
class A:
    def m(self):
        print("a -- m")

class B(A):
    def m(self):
        print("b -- m")


class C(A):
    def m(self):
        print("c -- m")

# 多继承
class D(C,B):
    def m(self):
        # 调用父级同名方法,执行顺序(继承列表顺序)
        super().m()# C
        # 通过类名调用实例方法,传递对象地址.
        # B.m(self)
        print("d -- m")

d01 = D()
d01.m()
print(D.mro())







