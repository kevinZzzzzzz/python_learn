"""
面向对象
    基于模板(类)去创建实体(对象)，使用对象完成功能开发
三大主要特性
    封装
    继承
    多态

私有成员：以__开头声明的变量即可完成设置仅供内部使用，而不对外开放的私有变量和私有方法  private
    私有成员无法被类对象使用，但是可以被类中其他的成员使用
"""


class Phone:
    __current_voltage = 0.1  # 当前手机的运行典雅
    def __keep_single_core(self):
        print('让CPU以单核模式运行')

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print('5g通话已开启')
        else:
            self.__keep_single_core()
            print('电量不足，无法开启5g通话，并已设置为单核运行进行省电')

phone = Phone()
# phone.__keep_single_core()  # AttributeError: 'Phone' object has no attribute '__keep_single_core'
# print(phone.__current_voltage)      # AttributeError: 'Phone' object has no attribute '__current_voltage'.
phone.call_by_5g()


class Phone1:
    __is_5g_enable = False

    def __check_5g(self):
        if self.__is_5g_enable:
            print('5g开启')
        else:
            print('5g关闭，使用4g网络')

    def call_by_5g(self):
        self.__check_5g()
        print('正在通话中')

phone1 = Phone1()
phone1.call_by_5g()