"""
    day10 复习
    封装:
        1. 封装数据:将多个基本类型复合为一个自定义类型.
                -- 优势:复合人类的思考方式
                        体现对数据的操作方式

        2. 封装功能:对外提供必要的功能,隐藏实现细节.
                -- 模块化的编程思想

        3. 分而治之,  封装变化,    高内聚,      低耦合.
            分解      变化点    类职责单一   类与类的关系松散

    MVC
"""
class StudentManagerController:

    def add_student(self):
        print("添加学生")


class StudentManagerView:

    def __init__(self):
        self.__manager = StudentManagerController()


    def input_student(self):
        # 调用逻辑控制器的实例方法
        # 语法:控制器对象地址.实例方法
        self.__manager.add_student()



















