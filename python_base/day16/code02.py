"""
    内置生成器：zip
"""

list02 = [101,102,103]
list03 = ["张三丰","张无忌","赵敏"]
for item in zip(list02,list03):
    # (101, '张三丰')
    print(item)

#练习：参照上述代码，自定义函数，my_zip  11:05
def my_zip(list01,list02):
    for index in range(len(list01)):
        # yield (list01[index],list02[index])
        yield list01[index], list02[index]

for item in my_zip(list02,list03):
    # (101, '张三丰')
    print(item)






