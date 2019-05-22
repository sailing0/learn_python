"""
    day16 复习
    生成器
        -- 特点：惰性操作／延迟操作（循环一次，计算一次，返回一次．）
        -- 本质: 迭代器　＋　可迭代对象
        -- 生成器函数：使用　yield　返回数据(结果有多个)
                    　使用　return　返回数据(结果有一个)
        -- 生成器表达式:(对变量的操作　for 变量　in 可迭代对象 if ..)

    函数式编程
        函数作为参数：将核心逻辑传入方法体，使方法适用性更广．
            -- lambda 语法：　lambda 参数:方法体　
           　
        *函数作为返回值：
"""
list01 = [33, 4, 55, 6, 7, 8]


def fun01():
    result = []
    for item in list01:
        if item > 5:
            result.append(item)
    return result


def fun02():
    for item in list01:
        if item > 5:
            # 生成器　告诉　客户端代码　的结果是右边item
            # 客户端代码　告诉　生成器　的信息是左边value
            value = yield item
            print("生成器收到:", value)


result01 = fun01()
result02 = fun02()

# print(result02)# 返回值是生成器对象　generator
# print(dir(result02))

# for item in result02:
#     print(item)

item = result02.__next__()
print(item)
while True:
    try:
        # item　是　yield 右侧返回的结果
        # item = result02.__next__()

        # item　是　yield 右侧返回的结果
        # send　参数是　yield 左边
        item = result02.send("qtx")
        print("客户端代码收到的是：", item)
    except:
        break


# 可迭代对象  迭代器
class MyGenerator:
    def __init__(self, target):
        self.target = target
        self.index = 0

    # 生成器具有当前方法，就是为了可以通过for获取结果．
    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.target) - 1:
            raise StopIteration()
        item = self.target[self.index]
        self.index += 1
        return item

    def send(self, value):
        if self.index > len(self.target) - 1:
            raise StopIteration()
        print("生成器收到：", value)
        item = self.target[self.index]
        self.index += 1
        return item


# for item in MyGenerator([3,4,4,5,7]):
#     print(item)

iterator = MyGenerator([3, 4, 4, 5, 7])
item = iterator.__next__()
print(item)
while True:
    try:
        # item　是　yield 右侧返回的结果
        # item = iterator.__next__()

        # item　是　yield 右侧返回的结果
        # send　参数是　yield 左边
        item = iterator.send("qtx")
        print("客户端代码收到的是：", item)
    except:
        break
