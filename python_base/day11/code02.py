"""
    继承语法 -- 数据
    # 练习: 定义父类--宠物, 数据:名字
    #     定义子类--狗, 数据:工作
    # 创建相应对象,画出内存图
"""

class Person:
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self,name,score):
        # 通过函数,调用父类方法
        super().__init__(name)
        self.score = score

class Teacher(Person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary

s01 = Student("zs",100)
print(s01.score)
print(s01.name)

p02 = Person("ww")
print(p02.name)




