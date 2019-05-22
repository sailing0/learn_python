# 一个球从100m的高度落下,每次弹回原高度的一半.
#    总共弹起多少次?(假定:最小弹起高度是0.01m)
#    总共走了多少米.

hight = 100  # 当前高度
count = 0  # 计时器
distance = hight  # 移动的距离
# hight / 2 弹起来高度 > 0.01
while hight / 2 >= 0.01:
    # 弹起来
    hight /= 2  # 高度减半
    count += 1
    print("第" + str(count) + "次弹起高度是:" + str(hight))
    distance += hight * 2  # *2  累加上下距离

print(count)
print(round(distance, 2))
