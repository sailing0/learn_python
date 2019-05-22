# 1. 自定义列表的排序函数
# 　　温馨提示：返回值需要吗？

def sort(list_target):
    # 传入的是可变类型
    # 修改的是传入的对象
    for r in range(len(list_target) - 1):
        for c in range(r+1,len(list_target)):
            if list_target[r] < list_target[c]:
                list_target[r],list_target[c] = list_target[c], list_target[r]
    # return list_target

# list01 = [2,4,4,5,6,7]
# re = sort(list01)
# print(re)

list01 = [2,4,4,5,6,7]
sort(list01)
print(list01)


