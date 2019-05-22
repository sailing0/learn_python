# 练习1:在控制台中获取一个商品单价  10
#      在获取一个商品数量   3
#      在获取一个金额  50
#      计算:应该找回多少钱 20

str_unit_price = input("请输入商品单价:")
int_unit_price = float(str_unit_price)
amount = int(input("请输入商品数量:"))
money = float(input("请输入金额:"))
result = money - int_unit_price * amount
print("应找回:"+str(result))


