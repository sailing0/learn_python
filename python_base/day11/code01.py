"""
    继承语法 -- 方法
    财产
    皇位

    #练习1:定义父类--宠物, 行为:吃
    #     定义子类--狗, 行为:防守xx
    #     定义子类--鸟, 行为:飞
    #创建相应对象,调用相应方法.测试isinstance,issubclass函数
    #14:35

"""


# 学生  与  老师  在某种概念上是统一的
# 学生是  人
# 老师是  人
#

class Person:
    def say(self):
        print("说")

class Student(Person):
    def study(self):
        print("学习")

class Teacher(Person):
    def teach(self):
        print("教")

s01 = Student()
s01.study()
# 可以直接使用父类成员
s01.say()

p02 = Person()
p02.say()
# 父类不能使用子类成员
# p02.study()

t03 = Teacher()
t03.teach()
# 不能使用"兄弟"类成员
# t03.study()

# 判断一个对象是否"兼容"一个类型
print(isinstance(s01,Person)) # True
print(isinstance(s01,Student)) # True
print(isinstance(s01,object)) # True

print(isinstance(s01,Teacher)) # False
print(isinstance(p02,Student)) # False

# 判断一个类是否"兼容"一个类型
print(issubclass(Student,Person)) # True
print(issubclass(Student,Teacher)) # False
print(issubclass(Student,(Teacher,Person))) # True
print(issubclass(Student,Student)) # True







