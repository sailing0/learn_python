"""
    内存图1.0
    不可变对象传参
"""


def fun01(num01):
    num01 = 2
    print("num01:" + str(num01))# 2


number01 = 1
# 调用方法,在内存中开辟空间(栈帧)
# 栈帧中定义该方法内部创建的变量
# 方法执行完毕后，栈帧立即释放．
fun01(number01)
print("number01:" + str(number01))# 1
