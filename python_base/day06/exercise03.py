# 练习：定义在控制台中显示矩形的函数　
def print_rect(r_count,c_count,char):
    for r in range(r_count):#      0        1        2
        for c in range(c_count):#01234    01234    01234
            print(char,end = "") # 在一行输出
        print() # 换行

print_rect(2,3,"*")
print_rect(5,2,"#")
# 参数:变量
#     函数调用者　　告诉　函数定义者的信息

