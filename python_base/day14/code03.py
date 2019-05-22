"""
    自定义异常
    练习:成绩异常(1-100)
"""

class AgeError(Exception):
    """
        封装错误信息
    """
    def __init__(self,msg,code,age_value):
        super().__init__(msg)
        self.msg = msg
        self.code = code
        self.age_value = age_value



class Wife:
    def __init__(self,age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if 20 <= value <= 30:
            self.__age = value
        else:
           # print("我不要")
           # raise ValueError("我不要") # 人为抛出异常
            raise AgeError("我不要",27,value)

try:
    w01 = Wife(80)
    print(w01.age)
except AgeError as e:
    print("错误信息:",e.msg)
    print("错误代码行号:",e.code)
    print("输入的年龄是:",e.age_value)
