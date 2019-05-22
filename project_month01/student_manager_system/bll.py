"""
    bll 业务逻辑层
"""
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