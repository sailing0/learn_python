"""
    练习：迭代员工管理器对象
    14:20
"""


class Employee:
    pass


class EmployeeIterator:
    """
        迭代器
    """
    def __init__(self, target):
        self.target = target
        self.index = 0

    def __next__(self):
        if self.index > len(self.target) - 1:
            raise StopIteration()
        item = self.target[self.index]
        self.index += 1
        return item


# 可迭代对象
class EmployeeManager:
    def __init__(self, employees):
        self.all_employee = employees

    def __iter__(self):
        # 返回迭代器
        return EmployeeIterator(self.all_employee)


manager = EmployeeManager([Employee(), Employee()])

# 需求：ｆｏｒ循环自定义类的对象
# for item in manager:
#     print(item)  #

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except:
        break
