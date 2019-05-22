class Enemy:
    def __init__(self, id, name, hp, atk, atk_speed):
        self.id = id
        self.name = name
        self.hp = hp
        self.atk = atk
        self.atk_speed = atk_speed

list01 = [
    Enemy(101,"玄冥大老",45,800,5),
    Enemy(102,"玄冥小老",40,700,3),
    Enemy(103,"qtx",800,1000,50),
    Enemy(104,"吕泽玛利亚",0,300,2),
    Enemy(105,"赵金多",500,900,10),
]

# for item in filter(lambda e: e.id > 102, list01):
#     print(item.id)

# for item in map(lambda e:e.name,list01):
#     print(item)

# for item in sorted(list01,key = lambda e:e.hp ):
#     print(item.hp)

# result = max(list01,key = lambda e:e.atk)
# print(result.name)

# 16:40 上课
# 练习１：查找血量在10--50之间的所有敌人
for item in filter(lambda e:10<= e.hp<= 50,list01):
    print(item.hp)

# 练习２：查找所有敌人的攻击力
for item in map(lambda e:e.atk,list01):
    print(item)

# 练习３：根据攻击力对敌人列表进行升序排列
for item in sorted(list01,key = lambda e:e.atk):
    print(item.atk)

# 练习４：查找姓名字数最长的敌人
result = max(list01,key=lambda e: len(e.name))
print(result.name)

