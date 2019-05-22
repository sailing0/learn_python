#练习2: 在控制台中获取一个4位整数1234
#    计算每位相加和  1+2+3+4  -->  10

int_number = int(input("请输入4位整数:"))
#1234
# unit01 = int_number  %  10
# unit02 = int_number // 10 % 10 # 1234 -->  123  -->  3
# unit03 = int_number // 100 % 10 # 1234 -->  12  -->  2
# unit04 = int_number // 1000
# result = unit01 + unit02 + unit03 + unit04
# print(result)

result = int_number  %  10
result += int_number // 10 % 10 # 1234 -->  123  -->  3
result += int_number // 100 % 10 # 1234 -->  12  -->  2
result += int_number // 1000
print(result)


