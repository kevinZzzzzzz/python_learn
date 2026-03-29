"""
自定义异常类
由开发人员自己定义的一个异常类，用来表示代码中"更具体，更有业务含义"的异常
具体规则，定义一个类（类名通常以Error结尾），继承Exception类或者其子类
"""

# class SchoolNameError(Exception):
#     pass
#
# SchoolNameError('学校名过长')


class SchoolNameError(Exception):
    def __init__(self, msg):
        super().__init__('【校名异常】' + msg)

raise SchoolNameError('学校名过长')
