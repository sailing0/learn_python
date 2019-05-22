# 在控制台中循环录入字符串，输入ｑ时退出．
# 　　然后显示一个新的字符串．

# str_result = ""
list_result = []
while True:
    str_input = input("请输入：")
    if str_input =="q":
        break
    # str_result = str_result + str_input
    # （１）使用列表拼接
    list_result.append(str_input)

#(2)　使用join合并
str_result = "".join(list_result)
print(str_result)


# 字符串　－－＞　列表
list01 = list("abc")
list01 = "a-b-c".split("-")
print(list01)













