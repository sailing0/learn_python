"""
    在控制台中获取一个总秒数
    计算几小时零几分钟零几秒钟.
"""
total_second = int(input("请输入总秒数:"))
second = total_second % 60 # 商指的是分钟数,余数指的是剩下的秒数
minute = total_second // 60 % 60# total_second // 60 商指的是分钟数,再除以60,商表示小时,余数表示剩下的分钟
hour = total_second // 3600
print(hour,minute,second)