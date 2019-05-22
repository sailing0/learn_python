# ２. 创建学生类
#     －－　数据：姓名，性别，年龄，成绩．
#     －－　行为：print_self()
#    画出学生列表内存图
#    定义函数：
#         －－　定义函数，在学生列表中，根据姓名查找学生对象．
#         －－　定义函数，在学生列表中，根据性别查找所有学生对象．
#         －－　查找年龄大于20，成绩大于60的所有学生对象．

class Student:
    def __init__(self,name,sex,age,score):
        self.name = name
        self.sex = sex
        self.age = age
        self.score = score

    def print_self(self):
        print(self.name,self.sex,self.age ,self.score)


list_stu = [
    Student("zs","男",25,60),
    Student("ls","女",28,86),
    Student("ww","男",40,100),
    Student("zl","女",18,95),
]


def get_student_for_name(list_target,name):
    for stu in list_target:
        if stu.name == name:
            return stu

# re01 = get_student_for_name(list_stu,"ls")
# re01.print_self()


# 在学生列表中，根据性别查找所有学生对象．
def get_students_for_sex(list_target,sex):
    # 使用列表存储多个结果
    result = []
    for stu in list_target:
        if stu.sex == sex:
            result.append(stu)
    return result

# re01 = get_students_for_sex(list_stu,"女")
# for item in re01:
#     item.print_self()

# result = []
# for stu in list_stu:
#     if stu.age >20 and stu.score > 60:
#         result.append(stu)

result = [stu for stu in list_stu if stu.age >20 and stu.score > 60]
for item in result:
    item.print_self()










