"""
    逻辑运算符  与and  或or   非not
               假     真      反
    身份运算符
"""

# 放学了  and   完成作业了    =两个条件都满足=>  回家了
# print(True and True)   # True
# print(False and False)# False
# print(True and False)# False
# print(False and True)# False
#
# print(1 > 2 and 5 > 3)# False
# print(1 < 2 and 5 > 3 and 10 > 5) # True

# 放学了  or   完成作业了    =满足其中一个条件即可=>  回家了
print(True  or True)   # True
print(False or False)# False
print(True  or  False)# True
print(False or True)# True

print(1 > 2 or 5 < 3 or 10 > 5)  # True
# 短路逻辑
# 如果第一个条件不满足  则不再考虑第二个条件
# print(1 > 2 and input("请输入:") == "a")
# 如果第一个条件满足  则不再考虑第二个条件
# print(1 > 2 or input("请输入:") == "a")
# 建议(启发):尽量将耗时的判断,放在后面.(因为很可能不执行)
# 身份运算符
num01 = 800
num02 = 900
num03 = num01
print(num01 is num02) # false
print(id(num01) ==  id(num02))
print(num03 is num01) #  true










