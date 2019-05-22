# 练习1：在控制台中录入学生成绩，计算总分，最高分，最低分。
# “请输入学生总数:”
# “请输入第1个学生成绩：”
stu_count = int(input("请输入学生总数:"))
list01 = []
for i in range(stu_count):
    score = int(input("请输入第%d个学生成绩："%(i+1)))
    list01.append(score)

print("总分：%d."%(sum(list01)))
print("最高分：%d."%(max(list01)))
print("最低分：%d."%(min(list01)))



