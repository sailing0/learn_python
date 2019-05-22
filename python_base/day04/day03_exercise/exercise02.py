# (扩展)在控制台中录入一个整数,判断是否为素数.
#    只能被1和自身整除的数字
#    例如:9
#        判断9能否被 2 --- 8 之间的数字整除
#        如果能,说明不是素数.3
#        如果都不能,说明是素数.

number = int(input("请输入整数:"))  # 9    2  ---  8

if number < 2:
    print("不是素数")
else:
    for i in range(2, number):
        if number % i == 0:
            print("不是素数")
            break  # 如果有结论了,就不需要在和后面的数字比较了
    else:
        print("是素数")
