"""
什么是python包
一个文件夹内，包含一个__init__.py文件，该文件夹可用于包含多个模块文件，从逻辑上看，包的本质是模块

步骤
1、新建包 my_package
2、新建包内模块: my_module1 和 my_module2
3、包含文件__init__.py
在__init__.py内可以通过__all__ = [] 控制允许导入的模块列表
"""

# import my_pageage.my_module1
# import my_pageage.my_module2
#
# my_pageage.my_module1.info_print1()
# my_pageage.my_module2.info_print2()

# from my_pageage import my_module1
# from my_pageage import my_module2
#
# my_module1.info_print1()
# my_module2.info_print2()

# from my_pageage.my_module1 import info_print1
# from my_pageage.my_module2 import info_print2
# info_print1()
# info_print2()

from my_pageage import *

my_module1.info_print1()
# my_module2.info_print2()  # 未解析的引用 'my_module2'

"""
安装第三方包- pip
pip install 包名称
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xxx 
"""