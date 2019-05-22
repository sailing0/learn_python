"""
    练习：　对象计数器　
        　创建老婆类(名字...)，随意实例化对象．
    　　　统计老婆数量（定义方法）
        　画出内存图
"""

class Wife:
    # 计数器
    count = 0

    @classmethod
    def get_count(cls):
        return Wife.count

    def __init__(self,name):
        # 实例变量
        self.name = name
        # 统计
        Wife.count += 1

w01 = Wife("王超")
w02 = Wife("马汉")
# 通过类名，访问类方法
print(Wife.get_count())








