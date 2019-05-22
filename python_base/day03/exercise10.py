# 练习: 随机加法考试
# 随机产生两个数字     8     10
# 在控制台中获取两个数字的相加结果 15
# 如果输入正确成绩累加10分
# 如果输入错误成绩扣除5分
# 总共5道题

import random

score = 0
for i in range(5):
    random_number01 = random.randint(1,10)
    random_number02 = random.randint(1,10)
    result_input = int(input("请计算:"+str(random_number01) +"+" + str(random_number02)+"=?"))
    if result_input == random_number01 + random_number02:
        score += 10
    else:
        score -= 5
print(score)


