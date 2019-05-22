# 2. 一家公司,有如下几种岗位:
#     普通员工:底薪
#     程序员:底薪 + 项目分红
#     销售员:底薪 + 销售额
#    定义员工管理器,记录所有员工,提供计算总薪资方法.
#    要求:增加新岗位,员工管理器代码不做修改.
#    体会:依赖倒置
class EmployeeManager:
    """
        员工管理器
    """

    def __init__(self):
        self.__all_employee = []

    def add_employee(self, employee):
        if not isinstance(employee, Employee):
            return
        self.__all_employee.append(employee)

    def get_total_salary(self):
        """
            计算总薪资
        :return:
        """
        total_salary = 0
        for item in self.__all_employee:
            # 编码期间:item 认为是员工
            # 运行期间:item 实际是具体员工
            total_salary += item.get_salary()
        return total_salary


class Employee:
    """
        员工类
        作用:代表具体员工,隔离员工管理器与具体员工的变化.
    """

    def __init__(self, name, salary):
        self.name = name
        self.base_salary = salary

    def get_salary(self):
        return self.base_salary


class Programmer(Employee):
    """
        程序员
    """

    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self):
        # return self.base_salary + self.bonus
        # 扩展重写
        return super().get_salary() + self.bonus


class Salesmen(Employee):
    """
        销售员
    """

    def __init__(self, name, salary, sale_value):
        super().__init__(name, salary)
        self.sale_value = sale_value

    def get_salary(self):
        return super().get_salary() + self.sale_value * 0.05


manager = EmployeeManager()
manager.add_employee(Employee("zs",3000))
manager.add_employee(Programmer("xp",4000,10))
manager.add_employee(Programmer("xx",99999,6135138))
manager.add_employee(Salesmen("pp",3000,500))

re = manager.get_total_salary()
print(re)

#练习:老王转岗
#     销售 -->  程序员
lw = Salesmen("老王",3000,500)
lw = Programmer("老王",8000,100000)

# 重新创建新对象,替换引用.好比是开除"老王",招聘新"老王"
# 要求:对象部分改变,而不是全部改变.





















