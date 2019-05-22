"""
    内置生成器：enumerate
"""

list01 = ["a", "b", "c"]

for item in enumerate(list01):
    # (索引,元素)
    print(item)

for index, element in enumerate(list01):
    print(index, element)

# 练习：参照上述代码，自定义函数，my_enumerate.
# 10:46

def my_enumerate(target):
    index = 0
    for item in target:
        yield (index,item)
        index += 1

for item in my_enumerate(list01):
    print(item)

for index, element in my_enumerate(list01):
    print(index, element)











