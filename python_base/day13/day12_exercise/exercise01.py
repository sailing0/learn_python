"""
    天龙八部技能系统
    设计原则:

"""

class ImpactEffect:
    """
        影响效果
        隔离技能释放器 与 具体的影响效果
    """
    def impact(self):
        # 要求子类必须实现,否则报错
        raise NotImplementedError()


class LowerDefense(ImpactEffect):
    """
        降低防御力
    """

    def __init__(self,distance,ratio):
        # 距离
        self.distance = distance
        # 比例
        self.ratio = ratio

    def impact(self):
        print("降低%d米内,目标的防御力为%d."%(self.distance,self.ratio))


class LowerSpeed(ImpactEffect):
    """
        降低速度
    """

    def __init__(self, time, ratio):
        # 时间
        self.time = time
        # 比例
        self.ratio = ratio

    def impact(self):
        print("降速为%.1f.时间是:%d" % (self.ratio, self.time))


class Damage(ImpactEffect):
    """
        伤害生命
    """

    def __init__(self, value):
        # 伤害值
        self.value = value

    def impact(self):
        print("伤害%d生命" % (self.value))


class SkillDeployer:
    """
        技能释放器
    """
    def __init__(self,name):
        self.name = name
        # 配置释放器,存储当前技能具有的所有影响效果对象
        self.__list_impact = self.__config_deployer()


    def __config_deployer(self):
        """
            配置释放器
        :return:
        """
        #*. 定义配置
        #1. 读取相应的影响效果
        #2. 创建影响效果对象
        # 依赖注入
        dict_skill_config = {
            "韦陀杵":["LowerDefense(10,0.5)","Damage(30)"],
            "降龙十八掌": ["LowerSpeed(5,0.2)", "Damage(80)"]
         }
        # ["LowerDefense(10,0.5)","Damage(30)"]
        # 根据键(技能名称)获取值(影响效果列表)
        list_impact_name = dict_skill_config[self.name]
        # list_impact = []
        # for item in list_impact_name:
        #     # 创建影响效果对象,并加入到列表中
        #     list_impact.append(eval(item))
        return [eval(item) for item in list_impact_name]


    def generate_skill(self):
        """
            生成技能
        :return:
        """
        print(self.name,"释放啦!")
        # 执行所有影响效果
        for item in self.__list_impact:
            # 编码期间:认为调用的是影响效果(父类ImpactEffect)
            # 运行期间:由于创建的是子类对象(伤害生命Damage...),所以执行的是子类方法.
            item.impact()

#--------测试---------------
# 创建技能对象
wei_tuo_chu = SkillDeployer("韦陀杵")
# 释放技能
wei_tuo_chu.generate_skill()


xiang_long_18_zhang = SkillDeployer("降龙十八掌")
xiang_long_18_zhang.generate_skill()



