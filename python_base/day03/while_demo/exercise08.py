"""
    猜数字1.0
    规则:系统产生1 -- 100 之间的随机数.
         让用户重复猜测,直到猜对了为止.
         提示:大了  小了    猜对了.

    猜数字2.0
    最多只能猜10次.
"""

import random

random_number = random.randint(1, 100)

# 1.0
# while True:
#     input_number = int(input("请输入:"))
#     if input_number > random_number:
#         print("大了")
#     elif input_number < random_number:
#         print("小了")
#     else:
#         print("猜对了")
#         break

# 2.0
count = 0
while count < 10:
    count += 1
    input_number = int(input("第"+str(count)+"次猜:"))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("猜对了")
        break
else:
    # 只有从while条件结束,才执行else语句.
    # (从循环体内部break,不会执行)
    print("没机会了你")

