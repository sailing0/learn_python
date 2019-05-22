# 4. 在控制台中获取圆形的半径
#    计算面积(3.14 * r 的平方)与周长(2 * 3.14 * r)
radius = float(input("请输入半径"))
area = 3.14 * radius ** 2
# length = 2 * 3.14 * radius# 31.400000000000002
# round()函数可以四舍五入
length = round(2 * 3.14 * radius, 3)
print("面积是:" + str(area) + ",周5长是:" + str(length))
