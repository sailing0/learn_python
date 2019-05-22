"""
    yield　－－＞　　生成器函数
"""

# class MyRange:
#     def __init__(self, stop):
#         self.stop = stop
#
#     def __iter__(self):
#         start = 0
#         while start < self.stop:
#             yield start
#             start += 1
#
# for item in MyRange(5):
#     print(item)

#17:05
# 生成器函数
def my_range(stop):
    start = 0
    while start < stop:
        yield start
        start += 1

# for item in my_range(5):
#     print(item)

iter01 = my_range(5)
for item in iter01:
     print(item)

