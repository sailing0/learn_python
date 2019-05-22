# 练习１：("悟空","八戒","沙僧","唐僧")
# 使用while + 迭代器　获取元组所有元素
t01 = ("悟空", "八戒", "沙僧", "唐僧")
iterator = t01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except:
        break

# 练习２：{"张三丰"：101,"张无忌":102,"赵敏":102}
# 不使用for循环，获取字典所有元素．

d01 = {"张三丰": 101, "张无忌": 102, "赵敏": 102}
iterator = d01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key, d01[key])
    except:
        break
