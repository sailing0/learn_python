"""
    运算符重载
"""

# print("a" + "b")
class Vector:
    """
        向量
    """
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return "向量的x变量是:%s"%self.x

    # 对象 +
    def __add__(self, other):
        return Vector(self.x + other)

    # + 对象
    def __radd__(self, other):
        return Vector(self.x + other)

    # 累加:在原有对象基础上进行操作,不创建新对象.
    def __iadd__(self, other):
        self.x += other
        return self

    def __lt__(self, other):
        return self.x  < other

v01 = Vector(10)
v02 = v01 + 5
# print(v02)
# 练习:实现向量类 与 整数 做 减法/乘法运算 17:25
v03 = 5 + v01
# print(v03)
v04 = v01 + v02
# print(v04)
# 练习:实现整数 与 向量 做 减法/乘法运算
#        向量    向量

list01 = [1]
list02 = list01 + [2]
print(list01)
list01 += [2]
print(list01)

print(id(v01))
# 累加含义:在原有对象基础上,增加新值
v01 += 1
print(v01)
print(id(v01))
# 练习:实现向量类 与 整数 做 累计减法/累计乘法运算

print(v01 < 2)