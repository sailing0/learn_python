"""
    生成器函数练习
    体会：方法／函数，需要向外返回多个结果时，使用生成器函数．
         惰性操作/延迟操作　(生成器函数的"循环(next)一次,计算一次,返回一次")

"""
list01 = [23,3,4,556,677,68,8,98,98]
# 练习１：在list01中，挑出所有偶数．
# 要求：1)使用生成器函数实现
def get_even01(target):
    for item in target:
        if item % 2 == 0:
            yield item

iter01 = get_even01(list01)# 没有执行方法体
for item in iter01:# 循环(next)一次,计算一次,返回一次
    print(item)

# def get_even02(target):
#     result = []
#     for item in target:
#         if item % 2 == 0:
#             result.append(item)
#     return result
#
# iter01 = get_even02(list01)# 执行方法体,将所有结果存在内存中．
# for item in iter01:
#     print(item)

# 练习２：定义函数，选出所有女同学.
class Student:
    def __init__(self,name,sex,age,score):
        self.name = name
        self.sex = sex
        self.age = age
        self.score = score

    def __str__(self):
        return "%s--%s--%d--%d"%(self.name,self.sex,self.age,self.score)

list_stu = [
    Student("张无忌","男",28,82),
    Student("赵敏","女",25,95),
    Student("周芷若","女",26,88),
]

def find_woman(target):
    for item in target:
        if item.sex == "女":
            yield item

for item in find_woman(list_stu):
    print(item)

# 练习３：选出所有成绩大于９０的学生
def find_by_score(target):
    for item in target:
        if item.score > 90:
            yield item

for item in find_by_score(list_stu):
    print(item)









