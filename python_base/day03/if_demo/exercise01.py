"""
    练习1:
    在控制台中获取一个月份
    打印季节(春1--3 夏4--6 秋7--9 冬10--12)
"""
month = int(input("请输入月份:"))
# if 1 <= month <= 3:
#     print("春天")
# elif 4 <= month <= 6:
#     print("夏天")
# elif 7 <= month <= 9:
#     print("秋天")
# elif 10 <= month <= 12:
#     print("冬天")

# if 1 <= month <= 3:
#     print("春天")
# elif 4 <= month <= 6:
#     print("夏天")
# elif 7 <= month <= 9:
#     print("秋天")
# elif 10 <= month <= 12:
#     print("冬天")
# else:
#     print("输入有误")

if month < 1 or month > 12:
    print("输入有误")
elif month <= 3:
    print("春天")
elif month <= 6:
    print("夏天")
elif month <= 9:
    print("秋天")
else:
    print("冬天")





