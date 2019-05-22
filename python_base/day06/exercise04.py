#练习：定义在控制台中显示直角三角形的函数
def print_triangle(height,char):
    """
        打印三角型
    :param height: 三角形高度
    :param char: 组成三角型的字符
    :return:
    """
    for r in range(height):
        for c in range(r+1):
            print(char, end="")
        print()

print_triangle(8,"*")
print_triangle(5,"#")
print_triangle(4,"?")












