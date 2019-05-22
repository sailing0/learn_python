# 练习: 下载double_list_helper.py模块
# 新建exercise01.py模块, 以3种方式, 测试工具类中的方法.

list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]

# 方式一
# re01 = double_list_helper.DoubleListHelper.get_elements(list01, double_list_helper.Vector2(1, 0), double_list_helper.Vector2.right(), 3)
re01 = helper.DoubleListHelper.get_elements(list01, helper.Vector2(1, 0), helper.Vector2.right(), 3)
print(re01)

# 方式二
# from double_list_helper import DoubleListHelper ,Vector2
# re01 = DoubleListHelper.get_elements(list01, Vector2(1, 0), Vector2.right(), 3)
# from double_list_helper import DoubleListHelper as helper ,Vector2 as vect
from double_list_helper import DoubleListHelper as helper
from double_list_helper import Vector2 as vect
re01 = helper.get_elements(list01, vect(1, 0), vect.right(), 3)
print(re01)

# 方式3
from double_list_helper import *
re01 = DoubleListHelper.get_elements(list01, Vector2(1, 0), Vector2.right(), 3)
print(re01)

