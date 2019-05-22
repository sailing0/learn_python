"""
    重构练习
"""


dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

list_order = []


def select_menu():
    """
        菜单选择　
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            buying()
        elif item == "2":
            settlement()

def settlement():
    """
        结算
    :return:
    """
    print_order()
    total_price = get_total_price()
    pay(total_price)

def pay(total_price):
    """
        支付
    :param total_price: 需要支付的价格
    :return:
    """
    while True:
        money = float(input("总价%d元，请输入金额：" % total_price))
        if money >= total_price:
            print("购买成功，找回：%d元。" % (money - total_price))
            list_order.clear()
            break
        else:
            print("金额不足.")


def print_order():
    """
        打印订单
    :return:
    """
    for item in list_order:
        commodity = dict_commodity_info[item["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], item["count"]))


def get_total_price():
    """
        计算总价
    :return:
    """
    total_price = 0
    for item in list_order:
        commodity = dict_commodity_info[item["cid"]]
        total_price += commodity["price"] * item["count"]
    return total_price


def buying():
    """
        购买
    :return:
    """
    print_commodity()
    order = create_order()
    list_order.append(order)
    print("添加到购物车。")


def create_order():
    """
        创建订单
    :return:
    """
    while True:
        cid = int(input("请输入商品编号："))
        if cid in dict_commodity_info:
            break
        else:
            print("该商品不存在")
    count = int(input("请输入购买数量："))
    return {"cid": cid, "count": count}


def print_commodity():
    """
        打印商品
    :return:
    """
    for key, value in dict_commodity_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))


# 程序入口
select_menu()














