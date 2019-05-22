"""
    ui 界面
    表示层
"""

from bll import *
from model import *


class StudentManagerView:
    """
        界面视图类
    """

    def __init__(self):
        # 创建逻辑控制器对象
        self.__manager = StudentManagerController()

    def __input_int(self, msg):
        while True:
            try:
                return int(input(msg))
            except:
                print("输入有误")

    def __input_students(self):
        # 1. 在控制台中录入学生信息,存成学生对象StudentModel.
        stu = StudentModel()
        stu.name = input("请输入姓名:")
        # while True:
        #     try:
        #         stu.age = int(input("请输入年龄:"))
        #         break
        #     except:
        #         print("输入有误")
        #
        # while True:
        #     try:
        #         stu.score = int(input("请输入成绩:"))
        #         break
        #     except:
        #         print("输入有误")
        stu.age = self.__input_int("请输入年龄:")
        stu.score = self.__input_int("请输入成绩:")

        # 2. 调用逻辑控制器的add_student方法
        self.__manager.add_student(stu)
        print(self.__manager)

    def __output_students(self, list_target):
        """
            显示学生列表信息
        :return:
        """
        # for stu in self.__manager.list_stu:
        for stu in list_target:
            # print(stu)
            print("%d -- %s -- %d -- %d" % (stu.id, stu.name, stu.age, stu.score))

    def __output_student_by_score(self):
        """
            根据成绩显示所有学生信息
        :return:
        """
        list_target = self.__manager.order_by_score()
        self.__output_students(list_target)

    def __delete_student(self):
        # id = int(input("请输入需要删除的学生编号:"))
        id = self.__input_int("请输入需要删除的学生编号:")
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        """
            修改学生信息
        :return:
        """
        stu = StudentModel()
        # stu.id = int(input("请输入需要修改的学生编号:"))
        stu.id = self.__input_int("请输入需要修改的学生编号:")
        stu.name = input("请输入姓名:")
        # stu.age = int(input("请输入年龄:"))
        # stu.score = int(input("请输入成绩:"))
        stu.age = self.__input_int("请输入年龄:")
        stu.score = self.__input_int("请输入成绩::")

        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("更新失败")

    def __display_menu(self):
        """
            显示菜单
        :return:
        """
        print("1) 添加学生")
        print("2) 显示学生")
        print("3) 删除学生")
        print("4) 修改学生")
        print("5) 按照成绩降序排列")

    def __select_menu(self):
        """
        选择菜单
        :return:
        """
        number = input("请输入选项:")
        if number == "1":
            self.__input_students()
        elif number == "2":
            self.__output_students(self.__manager.list_stu)
        elif number == "3":
            self.__delete_student()
        elif number == "4":
            self.__modify_student()
        elif number == "5":
            self.__output_student_by_score()

    def main(self):
        """
            界面入口方法
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()
