# 练习:在控制台中录入学生信息(姓名,年龄,性别,成绩)
# 在一行输出:
# 格式: 我的姓名是:xxx,年龄是:xxx,性别是:xxx,成绩是:xxx.
str_name = input("请输入姓名:")
str_age = input("请输入年龄:")
int_age = int(str_age)
str_sex = input("请输入性别:")
str_score = input("请输入成绩:")
float_score = float(str_score)

# int  不能 与 str  拼接
# print("我的姓名是:"+str_name+",年龄是:"+int_age+",性别是:"+str_sex + ",成绩是:"+float_score+".")

# 在固定格式的字符串中,插入不同类型的对象
print("我的姓名是:"+str_name+",年龄是:"+str(int_age)+",性别是:"+str_sex + ",成绩是:"+str(float_score)+".")










