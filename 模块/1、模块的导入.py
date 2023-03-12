"""
模块的导入方式
模块在使用前需要先导入，导入的语法如下
[from 模块名] import [模块｜类｜变量｜函数｜*] [as 别名]
常用的组合形式
import 模块名
from 模块名 import 类、变量、方法等
from 模块名 import *
import 模块名 as 别名
from 模块名 import 功能名 as 别名
"""

# 导入所有time模块 并使用sleep功能
import time

print('hello')
time.sleep(2)
print('world')

# 只导入time模块中的sleep功能
from time import sleep

print('start')
sleep(2)
print('end')

from time import *
print('1')
sleep(2)
print('2')

import time as t
print('hahe')
t.sleep(2)
print('heha')