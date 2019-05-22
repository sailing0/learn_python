# 练习2:在控制台中获取小时/分钟/秒,计算总秒数.
hour = int(input("请输入小时:"))
minute = int(input("请输入分钟:"))
second = int(input("请输入秒:"))
result = hour * 3600  + minute * 60 + second
print("总秒数是:"+str(result))


