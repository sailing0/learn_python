"""
    异常处理
    练习1:exercise02
    练习2: 将学生管理系统中可能出错的代码(转换为整数的代码),进行异常处理
"""


def div_apple(apple_count):
    # 分苹果
    person_count = int(input("请输入人数:"))  # ValueError
    result = apple_count / person_count  # ZeroDivisionError
    print("每个人分类%d个苹果" % result)


# 缺点:不能根据具体错误,做出相应处理逻辑.
# try:
#     div_apple(10)
# except Exception as e: # 捕获所有类型的异常
#     print("分苹果失败啦")


# try:
#     div_apple(10)
# except ValueError: # 捕获ValueError类型的异常
#     print("输入的人数有误")
# except ZeroDivisionError: # 捕获ZeroDivisionError类型的异常
#     print("人数不能是零")
# except Exception as e: # 捕获所有类型的异常
#     print("未知类型的错误")


try:
    div_apple(10)
except ValueError as e:  # 捕获ValueError类型的异常
    print("输入的人数有误")
except ZeroDivisionError:  # 捕获ZeroDivisionError类型的异常
    print("人数不能是零")
except Exception as e:  # 捕获所有类型的异常
    print("未知类型的错误")
else:  # 没有发生异常,执行的逻辑
    print("分苹果成功喽")
finally:
    print("无论是否发生异常,都执行的逻辑")
print("后续逻辑.......")
