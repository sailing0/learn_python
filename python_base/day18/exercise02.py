"""
    练习２：为两个已有功能(存款取款),添加新功能(验证账户)
    14:45
"""
def verify_accont(func):
    def wrapper(*args,**kwargs):
        print("验证账户")
        return func(*args,**kwargs)
    return wrapper

#deposit = verify_accont(deposit)
@verify_accont
def deposit(money):
    print("存款:",money)

@verify_accont
def withdraw():
    print("取钱")
    return 10000

deposit(5000)
print(withdraw())