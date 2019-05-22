"""
    选择语句
"""


sex = input("请输入性别:")
# if sex == "男":
#     print("您好,先生!")
# else:
#     print("您好,女士!")


# 错误逻辑,此时两段逻辑
# if sex == "男":
#     print("您好,先生!")
# if sex == "女":
#     print("您好,女士!")
# else:
#     print("性别未知")

if sex == "男":
    print("您好,先生!")
elif sex == "女":
    print("您好,女士!")
else:
    print("性别未知")








