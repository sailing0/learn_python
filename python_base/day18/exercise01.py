"""
    练习：使用装饰器实现：
    　　　为两个已有功能(进入后台，删除订单)，增加新功能（验证权限）.　
"""

# 1. 定义装饰器(新功能　＋　旧功能)

def verify_permissions(func):
    def wrapper(*args, **kwargs):
        print("验证权限")
        return func(*args, **kwargs)
    return wrapper

# 2. 拦截调用
@verify_permissions
def enter_background(loginId,pwd):
    print(loginId,pwd)
    print("进入后台系统.....")

@verify_permissions
def delete_order(order_id):
    print("删除%d订单..."%order_id)


enter_background("zs",123)
delete_order(101)


