# 练习1:在控制台中获取一个字符串,打印每个字符的编码值.
str_input  = input("请输入文字:")
for item in str_input:
    print(ord(item))

# 练习2:在控制台中循环输入编码值,显示字符.直到输入负数时,退出.
while True:
    number = int(input("请输入编码值:"))
    if number < 0:
        break
    print(chr(number))

