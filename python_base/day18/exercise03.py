"""
    练习：
    　　　为学生的学习方法，添加新功能(打印执行时间)
    15:40 上课
"""

import time


def print_execute_time(func):
    def wrapper(*args, **kwargs):
        # 记录执行前的时间
        start_time = time.time()
        result = func(*args, **kwargs)
        # 统计执行时间
        execute_time = time.time() - start_time
        print("执行时间是：", execute_time)
        return result

    return wrapper


class Student:
    def __init__(self, name):
        self.name = name

    @print_execute_time
    def study(self):
        print("开始学习喽")
        time.sleep(2)  # 睡眠两秒　模拟学习了两秒


s01 = Student("无忌")
s01.study()
