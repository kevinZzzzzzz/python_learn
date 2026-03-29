"""
模块概述
1、在python中，一个.py文件就是一个模块Module
2、模块中包含：变量、函数、类等多个内容
3、通常把能够实现的某个特定功能代码，集中放在一个模块中（模块类似一个工具箱）
4、模块可以提高代码的可维护性 与 可复用性，还可以避免命名冲突
 模块的分类
 python中的模块分为三类：标准库模型、自定义模块、第三方模块

 模块命名注意点
 1、符合标识符命名规则
 2、模块名.py文件名 区分大小写
 3、不要与标准库模块同名，python会优先引入标准库模块


 关于__all__
 在python模块中，可以通过__all__来控制【from 模块 import *】呢个导入哪些内容
 __all__的值可以是：列表、元组
"""
# 常见的模块导入方式
# import 模块名
import order
import pay
# print(order.max_order_amount)
#
# order.create_order()
# order.cancel_order()
# order.show_info()
# print('*' * 10)
# print(pay.timeout)
# pay.wechat_pay()
# pay.ali_pay()
# pay.show_info()

# import order as dd
#
# print(dd.max_order_amount)
# dd.create_order()
#
# from pay import show_info
#
# show_info()

from order import *
show_info()



import copy
print(copy.__file__)