"""
    实例成员
"""

# 创建实例成员，可以不在类中．（在实际项目中，仍然会在__init__方法中）
# class Wife01:
#     pass
#
#
# w01 = Wife01()
# w01.name = "丽丽"
# print(w01.name)
# print(w01.__dict__)# 此时实例变量是：{'name': '莉莉'}
#
# w01 = Wife01()
# print(w01.__dict__) # 此时实例变量是：｛｝


class Wife02:
    def __init__(self,name):
        self.name = name

w01 = Wife02("丽丽")
w01.name = "莉莉"
print(w01.__dict__)# 此时实例变量是：{'name': '莉莉'}
print(w01.name)

w01 = Wife02("丽丽")
print(w01.__dict__)# 此时实例变量是：{'name': '丽丽'}


# 创建实例成员，可以不在__init__中．（在实际项目中，仍然会在__init__方法中）
class Wife03:
    def __init__(self,name):
        self.name = name

    def fun01(self):
        self.age = 10
        print("fun01执行喽")

w01 = Wife03("丽丽")
# 通过对象调用实例方法，会自动传递对象地址．
w01.fun01()
# 通过类名调用实例方法，
Wife03.fun01(w01)
print(w01.age)








