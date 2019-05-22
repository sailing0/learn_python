"""
    练习：画出下列代码内存图
"""

def fun01(a,b,c):
    a = 100
    # 修改的是列表对象，
    b[0] = 200
    # 修改的是栈帧中的变量
    c = 300

num01 = 1
list01 = [2]
list02 = [3]
fun01(num01,list01,list02)

print(num01)#? 1
print(list01)#?　２００
print(list02)#?　３
