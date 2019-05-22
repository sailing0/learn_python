"""
    程序入口
"""
from ui import *

# 从当前模块运行,执行程序逻辑.
if __name__ == "__main__":
    try:
        view = StudentManagerView()
        view.main()
    except:
        print("...")
