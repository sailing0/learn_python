# 练习:在控制台获取一个变量
#      再获取一个变量
#      让两个变量交换.
#      输出结果

input01 = input("请输入第一个变量:")
input02 = input("请输入第二个变量:")
# 利用临时变量进行交换
# temp = input01
# input01 = input02
# input02 = temp

# 直接交换
# input01 , input02 = 222,111
input01, input02 = input02, input01

print("第一个变量是" + input01)
print("第二个变量是" + input02)
