"""
继承分为单继承和多继承 extents
单继承的写法
    class 类名(父类名):
        内容

多继承写法
    class 类名(父类1，父类2，。。。)
    注意事项
        如有同名的成员，那么默认以继承顺序(从左到右)为优先级
        先继承的保留，后继承的被覆盖
"""
class Phone:
    IMEI = None     # 序列号
    producer = None     # 厂商

    def call_by_4g(self):
        print('4g通话')

class Phone2022(Phone):
    face_id = True      # 面部识别

    def call_by_5g(self):
        print('202 2最新5g通话')

phone = Phone()
phone.call_by_4g()

phone2022 = Phone2022()
phone2022.call_by_4g()
phone2022.call_by_5g()

class NFCReader:
    nfc_type = '第五代'
    produer = 'kevinzzzzzz'

    def read_card(self):
        print('读取NFC')

    def write_card(self):
        print('写入NFC')

class RemoteControl:
    rc_type = '红外遥控'
    produer = 'kevinzzzzzz11111'

    def control(self):
        print('红外遥控开启')

class MyPhone(Phone, NFCReader, RemoteControl):
    pass  # 关键字 补全语法，不产生错误

myPhone = MyPhone()
myPhone.call_by_4g()
myPhone.read_card()     # 先继承的保留，后继承的被覆盖

print(myPhone.producer)

"""
复写
    子类继承父类的成团属性和方法后，可以进行重新定义使用
super 调用父类同名成员
    如果复写后需要调回原来父类的成员
    方式一：父类名.变量/方法(self)
    方式二：super().变量/方法()
"""
class Phone2:
    IMEI = None     # 序列号
    producer = 'kevinZzzz'     # 厂商

    def call_by_4g(self):
        print('4g通话')

class MyPhone2(Phone2):
    pruducer = "kevinZzzz2222"

    def call_by_4g(self):
        Phone2.call_by_4g(self)
        super().call_by_4g()
        print(f'父类的厂商：{super().producer}')
        print('子类的4g通话')


myPhone2 = MyPhone2()
myPhone2.call_by_4g()