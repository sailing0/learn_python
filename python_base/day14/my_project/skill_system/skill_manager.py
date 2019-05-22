"""
    skill_manager

"""

from skill_system.skill_deployer import *

class SkillManager:
    def create_skill(self):
        print("SkillManager -- create_skill")

SkillDeployer().generate_skill()

# 只能从当前模块开始运行,才能成功导入skill_deployer模块
# 如果从主模块开始运行,导入错误.
# from skill_deployer import SkillDeployer
# SkillDeployer().generate_skill()