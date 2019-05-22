# 练习１：在控制台中随意录入多个字符串．
#        按ｑ退出，再显示所有不重复的字符串．

set_target = set()
while True:
    str_input = input("请随意输入：")
    if str_input == "q":
        break
    set_target.add(str_input)

for item in set_target:
    print(item)




