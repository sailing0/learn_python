# 定义函数，整数相加的函数。
def add(*args):
    sum = 0
    for item in args:
        sum += item
    return sum

re = add(1,2,3,4,45,43)
print(re)
