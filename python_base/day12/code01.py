
class Employee:
    """
        员工类
    """

    def __init__(self, name,job):
        self.name = name
        # 成员变量的类型是岗位
        self.job = job

    def calculate_salary(self):
        """
            使用岗位,计算薪资.
        :return:
        """
        return self.job.get_salary()

class Job:
    """
        岗位
    """
    def __init__(self,salary):
        self.base_salary = salary

    def get_salary(self):
        return self.base_salary

class Programmer(Job):
    """
        程序员
    """

    def __init__(self,salary, bonus):
        super().__init__(salary)
        self.bonus = bonus

    def get_salary(self):
        # return self.base_salary + self.bonus
        # 扩展重写
        return super().get_salary() + self.bonus


class Salesmen(Job):
    """
        销售员
    """

    def __init__(self,salary, sale_value):
        super().__init__(salary)
        self.sale_value = sale_value

    def get_salary(self):
        return super().get_salary() + self.sale_value * 0.05

#练习:老王转岗
#     销售 -->  程序员
# 继承关系
# lw = Salesmen("老王",3000,500)
# lw = Programmer("老王",8000,100000)

# 重新创建新对象,替换引用.好比是开除"老王",招聘新"老王"
# 要求:对象部分改变,而不是全部改变.


lw = Employee("老王",Salesmen(3000,500))
print(lw.calculate_salary())
# 转岗
lw.job = Programmer(8000,100000)
print(lw.calculate_salary())













