# 练习：定义检查列表是否具有相同元素的方法
def is_repeating(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] == list_target[c]:
                return True # 退出方法(可以退出两层循环)
    return False
re01 = is_repeating([3,44,5])
re01 = is_repeating([3,44,5,44])
print(re01)
