# 练习: 在控制台中显示120秒倒计时
# 02:00  01:59  .......   00:00
for second in range(120, -1, -1):
    print("%02d:%02d" % (second // 60, second % 60))

list0 = [1, [2,3]]
list1 = list0.copy()
list0[1][0] = 100
print(list1[1][0])
