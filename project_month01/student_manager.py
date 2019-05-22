"""
    学生管理器系统
"""


class StudentModel:
    """
        学生数据模型类
    """

    def __init__(self, name="", age=0, score=0, id=0):
        """
            创建学生对象
        :param id: 编号
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        """
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value


class StudentManagerController:
    """
        学生逻辑控制器
    """

    def __init__(self):
        self.__list_stu = []

    @property
    def list_stu(self):
        return self.__list_stu

    def add_student(self, stu):
        """
            添加新学生
        :param stu: 需要添加的学生对象
        """
        stu.id = self.__generate_id()
        self.__list_stu.append(stu)

    def __generate_id(self):
        # 生成编号的需求:新编号,比上次添加的对象编号多1.
        # if len(self.__list_stu) > 0:
        #     id = self.__list_stu[-1].id + 1
        # else:
        #     id = 1
        # return id
        return self.__list_stu[-1].id + 1 if len(self.__list_stu) > 0 else 1

    def order_by_score(self):
        """
            根据成绩升叙排列
        :return:
        """
        # 创建新列表(目的:不影响原有列表)
        new_list = self.__list_stu[:]
        for r in range(len(new_list) - 1):
            for c in range(r + 1, len(new_list)):
                if new_list[r].score > new_list[c].score:
                    new_list[r], new_list[c] = new_list[c], new_list[r]
        return new_list

    def remove_student(self, id):
        """
            删除学生
        :param id:
        :return:
        """
        for stu in self.list_stu:
            if stu.id == id:
                self.list_stu.remove(stu)
                return True  # 表示删除成功
        return False  # 表示删除失败

    def update_student(self, stu):
        """
            更新学生信息
        :return:
        """
        for item in self.__list_stu:
            if item.id == stu.id:
                item.name = stu.name
                item.score = stu.score
                item.age = stu.age
                return True
        return False


# controller = StudentManagerController()
# controller.add_student(StudentModel("zs",18,85))
# controller.add_student(StudentModel("zs",18,85))
# for item in controller.list_stu:
#     print(item.id,item.name,item.age,item.score)

class StudentManagerView:
    """
        界面视图类
    """

    def __init__(self):
        # 创建逻辑控制器对象
        self.__manager = StudentManagerController()

    def __input_students(self):
        # 1. 在控制台中录入学生信息,存成学生对象StudentModel.
        stu = StudentModel()
        stu.name = input("请输入姓名:")
        stu.age = int(input("请输入年龄:"))
        stu.score = int(input("请输入成绩:"))
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
        id = int(input("请输入需要删除的学生编号:"))
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
        stu.id = int(input("请输入需要修改的学生编号:"))
        stu.name = input("请输入姓名:")
        stu.age = int(input("请输入年龄:"))
        stu.score = int(input("请输入成绩:"))
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


view = StudentManagerView()
view.main()
