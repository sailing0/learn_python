"""
    练习：
"""

class Enemy:
    """
        敌人
    """
    def __init__(self,name = "",hp = 0,atk = 0.0,atk_speed = 0.0):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.atk_speed = atk_speed

    def print_self(self):
        print(self.name,self.hp,self.atk,self.atk_speed)

#　练习：
# 1. 在控制台中输入３个敌人，存入列表．
# 2. 将敌人列表输出（调用print_self）到控制台

# e01 = Enemy("zs",100,1000,5)
# list_enemy = []
# for i in range(3):
#     e = Enemy()
#     e.name = input("请输入姓名：")
#     e.hp = int(input("请输入血量："))
#     e.atk = float(input("请输入攻击力："))
#     e.atk_speed = float(input("请输入攻击速度："))
#     list_enemy.append(e)
#
# for item in list_enemy:
#     item.print_self()

# 练习３：定义函数，在敌人列表中，根据姓名查找敌人对象．
# e01 = Enemy("zs",100,10,2)
# e02 = Enemy("ls",200,5,3)
# e03 = Enemy("ww",300,8,5)
#
# list_enemy = [e01,e02,e03]

def get_enemy_for_name(list_enemy,name):
    # 遍历敌人列列表
    for item in list_enemy:
        # 如果有指定名称的敌人对象
        if item.name == name:
            # 则返回对象地址
            return item

list01 = [
    Enemy("zs",100,10,2),
    Enemy("ls", 200, 5, 3),
    Enemy("ww",300,8,5)
]

re = get_enemy_for_name(list01,"ls")
if re != None:
    re.print_self()
else:
    print("没有找到")


