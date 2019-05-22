"""
    循环语句
        -- while
"""
# while 条件:
#     执行代码
#     if 退出条件1:
#         break
# 死循环:条件永远满足的循环
while True:
    str_usd = input("请输入美元")
    float_usd = float(str_usd)
    rmb = float_usd * 6.708
    print(rmb)
    if input("按e键则退出") =="e":
        break # 退出循环体
print(".....")




