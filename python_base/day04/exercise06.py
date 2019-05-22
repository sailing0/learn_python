# 练习2：在控制台中录入学生姓名。　　
#       要求：姓名不能重复
#            如果录入esc,则停止录入，打印每个学生姓名．17:05

list_names = []

while True:
    name = input("请输入第%d个学生姓名：" % (len(list_names) + 1))
    if name == "esc":
        break
    # 如果姓名不存在：
    if name not in list_names:
        list_names.append(name)

for item in list_names:
    print(item)
