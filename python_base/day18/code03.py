"""
    装饰器
     -- 闭包的应用
     练习:exercise01
"""

# def say_hello():
#     print("hello")
#
#
# def say_goodbye():
#     print("goodbye")
#
#
# say_hello()
# say_goodbye()


# 需求：在两个方法实现的功能基础上，增加新功能(打印方法名称)

# def say_hello():
#     print(say_hello.__name__)
#     print("hello")
#
#
# def say_goodbye():
#     print(say_goodbye.__name__)
#     print("goodbye")
#
#
# say_hello()
# say_goodbye()

# 缺点：代码重复.
# 解决：提取打印方法名称的功能

# def print_func_name(func):
#     print(func.__name__)
#
# def say_hello():
#     # print(say_hello.__name__)
#     print_func_name(say_hello)
#     print("hello")
#
#
# def say_goodbye():
#     # print(say_goodbye.__name__)
#     print_func_name(say_goodbye)
#     print("goodbye")

# say_hello()
# say_goodbye()
# 缺点：在两个已有功能的内部，增加新功能，代码可读性差．

# def say_hello():
#     # print_func_name(say_hello)
#     print("hello")

# def say_goodbye():
#     # print_func_name(say_goodbye)
#     print("goodbye")
#
# def print_func_name(func):
#     # 包装新旧功能
#     def wrapper():
#         # 增加的新功能
#         print(func.__name__)
#         # 旧功能
#         func()
#
#     return wrapper # 返回包装器
#
# say_hello = print_func_name(say_hello)
# say_goodbye = print_func_name(say_goodbye)
#
# say_hello()
# say_goodbye()

# 缺点：调用者完成包装新旧方法的任务．
# 解决：应该有定义者完成．

# def print_func_name(func):
#     # 包装新旧功能
#     def wrapper():
#         # 增加的新功能
#         print(func.__name__)
#         # 旧功能
#         func()
#
#     return wrapper # 返回包装器
#
# @print_func_name # say_hello = print_func_name(say_hello)
# def say_hello():
#     print("hello")
#     return "哈哈"
#
# @print_func_name
# def say_goodbye():
#     print("goodbye")
#
# #---------以上是定义者--以下是调用者-----------------
# say_hello()
# say_goodbye()

# 缺点：旧功能的返回值不能被客户端代码接受到．
#      旧功能的参数，客户端代码也无法传入.

# def print_func_name(func):
#     # 包装新旧功能
#     def wrapper(name):
#         # 增加的新功能
#         print(func.__name__)
#         # 旧功能
#         return func(name)
#
#     return wrapper # 返回包装器

# 缺点：包装器不能适应所有的旧功能参数
def print_func_name(func):
    # 包装新旧功能
    def wrapper(*args,**kwargs):
        # 增加的新功能
        print(func.__name__)
        # 旧功能
        return func(*args,**kwargs)

    return wrapper # 返回包装器

@print_func_name # say_hello = print_func_name(say_hello)
def say_hello(name):
    print(name,"hello")
    return "哈哈"

@print_func_name
def say_goodbye(name,age):
    print(age,name,"goodbye")

#---------以上是定义者--以下是调用者-----------------
print(say_hello("张无忌"))
say_goodbye("赵敏",25)
