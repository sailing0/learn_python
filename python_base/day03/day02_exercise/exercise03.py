# 5.修改exercise03中的练习,如果金额不足,提示还差多少钱,如果金额够,提示应找回多少钱.
# -- 尝试:如果总价到达100元,打八折.

str_unit_price = input("请输入商品单价:")
int_unit_price = float(str_unit_price)
amount = int(input("请输入商品数量:"))
money = float(input("请输入金额:"))
# 总金额
total_price = int_unit_price * amount
# 满足条件打折
if total_price >= 100:
    total_price /= 0
# 如果钱够
if money > total_price:
    result = money - total_price
    print("应找回:"+str(result))
else:
    print("还差"+str(total_price - money)+"钱")
# 调试:让程序在指定的行中断,然后逐语句执行,我们审查程序运行过程,以及变量的取值.
# 1. 在可能出错的行,加入断点.
# 2. 开始调试 Alt + Shift + F9
# 3. 命中断点后(断点行是蓝色的),逐语句执行F7.
# .....(判断执行过程,以及变量取值).....
# 4. 停止调试Ctrl + F2




