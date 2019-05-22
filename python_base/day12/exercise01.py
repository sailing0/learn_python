# 练习: 重写 StudentModel 类 __str__ 方法 与__repr__方法
#  创建学生对象,创建学生对象列表.分别print

class StudentModel:
    def __init__(self, name="", age=0, score=0, id=0):
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return "我的编号是:%d,姓名是:%s,年龄是:%d,成绩是:%d."%(self.id,self.name,self.age,self.score)

    def __repr__(self):
        return 'StudentModel("%s",%d,%d)'%(self.name,self.age,self.score)

s01 = StudentModel("zs",24,100)
s02 = eval(s01.__repr__())
print(s02)
print(s01)
list01 = [s01,s02]
print(list01)
