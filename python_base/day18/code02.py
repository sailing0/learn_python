"""
    闭包

"""

def fun01():
    print("fun01执行喽")
    a = 1
    def fun02():
        print("fun02执行喽")
        print("外部变量是:",a)
    return fun02

# 得到的是内部函数
result = fun01()
# 调用内部函数，因为内部函数使用了外部变量，所以称之为闭包．
result()# 可以使用外部变量，说明外部函数在调用后没有释放．

# 案例：

def give_gift_money(money):
    """
        获取压岁钱
    """
    print("得到了%d压岁钱"%money)
    def child_buy(target,price):
        """
            孩子需要买东西
        """
        nonlocal money
        if money >=  price:
            money -= price
            print("孩子花了%d钱，买了%s,还剩下%d钱．"%(price,target,money))
        else:
            print("压岁钱不够了")
    return child_buy

action = give_gift_money(10000)
action("98k",3500)
action("小猪佩奇",300)
action("大黄蜂",8000)

# 体会：闭包使得逻辑连续（因为内部函数可以使用外部变量）．

