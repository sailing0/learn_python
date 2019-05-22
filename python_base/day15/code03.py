"""
    迭代器 --> yield
    练习：exercise04/exercise05
"""

class Skill:
    pass


# class SkillIterator:
#     """
#         技能迭代器
#     """
#     def __init__(self, target):
#         self.target = target
#         self.index = 0
#
#     def __next__(self):
#         if self.index > len(self.target) - 1:
#             raise StopIteration()
#         item = self.target[self.index]
#         self.index += 1
#         return item


class SkillManager:
    def __init__(self, skills):
        self.skills = skills

    # def __iter__(self):
    #     return SkillIterator(self.skills)

    def __iter__(self):
        """
            执行过程：
            １．调用__iter__()方法不执行
            ２．调用__next__()方法时执行，到yield语句暂时离开．
            ３．再次调用__next__()方法时，从上次离开的代码开始执行，到yield语句暂时离开
            4. 待执行完方法体，抛出StopIteration异常．

            原理：如果方法体中包含yield关键字，那么会自动生成迭代器对象．
            生成迭代器代码的大致规则：　
            1. 将yield关键字以前的代码，放到__next__方法中．
            2. 将yield关键字以后的数据，作为__next__方法的返回值
        """
        # print("准备返回第一个元素")
        # yield self.skills[0]  # 暂时离开点　　　再次执行点
        #
        # print("准备返回第二个元素")
        # yield self.skills[1]
        #
        # print("准备返回第三个元素")
        # yield self.skills[2]

        for item in self.skills:
            yield item



#---------------以下是客户端代码---------------------

manager = SkillManager([Skill(), Skill(), Skill()])

# for item in manager:
#     print(item)

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except Exception as e:
        print(e)
        break


# 练习：改写上节课练习（员工管理器／ＭｙＲａｎｇｅ），将迭代器转换为yield
# 通过断点调试，体会程序执行过程，与生成迭代器代码的原理．
# 16:20














