"""
    类成员
    练习:exercise01
"""
class ICBC:
    """
        工商银行
    """
    # 类变量    相当于被大家共享的"饮水机",
    moneys = 9999999

    # 类方法
    @classmethod
    def print_total_moneys(cls):
        # print(ICBC.moneys)
        print("总行金额：",cls.moneys)

    # 实例方法
    def __init__(self,name,money):
        # 实例变量：相当于每个人的"杯子"
        self.money = money
        self.name = name
        # 从总行中，扣除当前支行的现金
        ICBC.moneys -= money

i01 = ICBC("广渠门支行",100000)
# 调用类变量
# print("总行金额：",ICBC.moneys)
# 调用类方法，此时会自动传递类名进入方法
ICBC.print_total_moneys()

i02 = ICBC("磁器口支行",100000)
# print("总行金额：",ICBC.moneys)
ICBC.print_total_moneys()









