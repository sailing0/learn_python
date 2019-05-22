"""
     改造为yield实现
"""


# class MyRangeIterator:
#     def __init__(self, stop):
#         self.stop = stop
#         self.start = 0
#
#     def __next__(self):
#         if self.start + 1 > self.stop:
#             raise StopIteration()
#         temp = self.start
#         self.start += 1
#         return temp


class MyRange:
    def __init__(self, stop):
        self.stop = stop

    # def __iter__(self):
    #     # 创建迭代器对象
    #     return MyRangeIterator(self.stop)

    def __iter__(self):
        start = 0
        while start < self.stop:
            yield start
            start += 1


iterator = MyRange(5)
# for item in iterator:
#     print(item)  #

iterator = iterator.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except:
        break
