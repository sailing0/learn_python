"""
    标准库模块 -- 时间
    练习:exercise02
"""
import time

# 返回时间戳(1970年后经过的浮点秒数)
# 1555579061.7284493
print(time.time())

# 时间戳 --> 时间元组(年  月   日   时  分   秒   星期    一年的第几天   夏令时)
print(time.localtime(1555579061.7284493))

# 时间元组  --> 时间戳
print(time.mktime(time.localtime()))

# 时间元组 -->  字符串 (时间的格式化)
# time.localtime()  -->  str
print(time.strftime("%Y %m %d  %H:%M:%S", time.localtime()))
print(time.strftime("%y %m %d  %H:%M:%S", time.localtime()))

# 字符串 -->  时间元组
print(time.strptime("2019 04 14", "%Y %m %d"))
