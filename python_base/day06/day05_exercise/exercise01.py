# 4. 在控制台中录入5个学生信息(姓名／年龄／性别)
# 数据结构：列表中嵌套字典
# [
#     {
#         "name":xx,
#         "age":xx,
#         "sex":xx,
#     },
#     {
#         "name":xx,
#         "age":xx,
#         "sex":xx,
#     }
#     .......
# ]

list_student_info = []
for i in range(2):
    # 每次循环创建一个新字典表示一个新学生
    dict_student = {}
    dict_student["name"] = input("请输入姓名：")
    dict_student["age"] = int(input("请输入年龄："))
    dict_student["sex"] = input("请输入性别：")
    # 向学生列表追加学生信息
    list_student_info.append(dict_student)


# 获取所有学生信息
for dict_stu in list_student_info:
    for key,value in dict_stu.items():
        print("%s -- %s"%(key,value))














