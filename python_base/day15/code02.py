"""
    迭代器
    练习：exercise02/exercise03
"""


class Skill:
    pass


class SkillIterator:
    """
        技能迭代器
    """
    def __init__(self, target):
        self.target = target
        self.index = 0

    def __next__(self):

        # 如果索引越界　则抛出异常
        if self.index > len(self.target) - 1:
            raise StopIteration()
        # 返回下一个元素
        item = self.target[self.index]
        self.index += 1
        return item


class SkillManager:
    """
        可迭代对象
    """
    def __init__(self, skills):
        self.skills = skills

    def __iter__(self):
        # 创建迭代器对象  传递　需要迭代的数据
        return SkillIterator(self.skills)


#---------------以下是客户端代码---------------------

manager = SkillManager([Skill(), Skill(), Skill()])
# for item in manager.skills:
for item in manager:# 获取manager对象中列表元素(获取manager对象的聚合类型对象元素)
    print(item)
# iterator = manager.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except:
#         break
