"""
    (1)学生student是一个类，具有姓名，年龄等数据；
    具有学习study，工作work等行为。
    对象：悟空同学，28岁。
          八戒同学，29岁。

"""
class Student:
    """
        学生类
    """
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self):
        print(str(self.age) + "学习")

    def work(self):
        print(self.name+"工作")

# s01 悟空对象的地址
s01 = Student("悟空",28)
s02 = Student("八戒",29)

# 通过对象地址，调用对象方法，会自动传递对象地址．
s01.study()
s02.work()




# s01 = Student("悟空",28)
# s02 = s01
# s01.name = "孙悟空"
# print(s02.name) # ?

s01 = Student("悟空",28)
s02 = s01
s01 = Student("八戒",28)
s01.name = "孙悟空"
print(s02.name) # ? 悟空













