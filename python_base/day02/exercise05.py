#练习3:古代的称一斤16两
# 在控制中获取两,换算出是几斤零几两.
total_liang = int(input("请输入总两数:"))
jin = total_liang // 16
liang = total_liang % 16
print(str(jin) +"斤零"+str(liang)+"两")