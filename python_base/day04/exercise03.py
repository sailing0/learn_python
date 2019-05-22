#练习:在控制台中,获取一个字符串.
#1.  打印第一字符
#2.  打印最后一个字符
#3.  如果是奇数,打印中间的字符串(len(字符串))
#4.  打印倒数3个字符
#5.  倒叙打印字符串

# str_input = input("请输入字符串:")
str_input = "abcde"
#1.  打印第一字符
print(str_input[0])
# print(str_input[-len(str_input)])
#2.  打印最后一个字符
print(str_input[-1])
# print(str_input[len(str_input) - 1])
#3.  如果是奇数,打印中间的字符串(len(字符串))
if len(str_input) % 2 == 1:
    print(str_input[len(str_input) // 2])
#4.  打印倒数3个字符
print(str_input[-3:])
#5.  倒叙打印字符串
print(str_input[::-1])

