"""
    有若干个图形(圆形,矩形........)
    每种图形,都可以计算面积.
    定义图形管理器,记录所有图形,提供计算总面积的方法.
    要求:增加新的图形,不改变图形管理器代码.
"""

class GraphicManager:
    def __init__(self):
        # 记录所有图形
        self.__graphics = []

    def add_graphic(self,g):
        if not isinstance(g,Graphic):
            return
        self.__graphics.append(g)

    def get_total_area(self):
        """
            计算总面积
        :return:
        """
        total_area = 0
        for item in self.__graphics:
            # 调用:父类
            # 执行:子类
            total_area += item.get_area()
        return total_area


class Graphic:
    """
        图形
    """
    def get_area(self):
        pass

class Circle(Graphic):
    """
        圆形
    """
    def __init__(self,radius):
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * 3.14


class Rectangle(Graphic):
    """
        矩形
    """

    def __init__(self, length,width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length  * self.width


manager = GraphicManager()
manager.add_graphic("ok")
manager.add_graphic(Rectangle(2,3))
manager.add_graphic(Circle(5))
# 加断点,调试
print(manager.get_total_area())


