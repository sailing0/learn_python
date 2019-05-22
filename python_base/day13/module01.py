"""
    文档字符串
"""

# 可以导出
__all__ = ["fun01","MyClass01"]

# 只在第一次被导入时执行
print("我是module01")

def fun01():
    print("fun01")


class MyClass01:
    def fun02(self):
        print("fun02")

def _fun03():
    print("fun03")

def fun04():
    print("fun04")