"""
    module01
"""

def fun01():
    print("module01 -- fun01")


# 调用 module02
from package01.package02.module02 import *

fun02()