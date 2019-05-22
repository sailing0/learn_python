"""
    内置可重写函数
    练习:exercise01.py
"""

class Wife:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        # 返回给人看
        return "奴家叫:%s,年芳:%d"%(self.name,self.age)
    def __repr__(self):
        # 返回给解释器看
        return 'Wife("%s",%d)'%(self.name,self.age)

w01 = Wife("金莲",25)
print(w01)# 将对象转换为字符串
# re = eval("1 + 5")
# print(re)
# w02 = eval('Wife("金莲",25)')
# w03 = eval(input(""))
#创建了新对象
w02 = eval(w01.__repr__())
print(w02)
w01.name ="莲莲"
print(w02.name)











