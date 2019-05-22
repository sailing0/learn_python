# 练习:定义方法,在控制台中获取成绩int(1 -- 100)
#      要求:如果输入有误,重新输入.
def get_score():
    while True:
        try:
            number = int(input("请输入成绩:"))
        # except ValueError:
        except:
            print("输入有误")
            continue # 跳过本次循环

        if 1<= number <= 100:
            return number

        print("成绩不在范围内")
get_score()
