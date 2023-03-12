"""
类型注解   同ts   但是没有类型校验
    基础语法： 变量:类型
            def 函数名(形参名：类型，。。。。。) -> 返回值类型:
                。。。。
    联合类型：
        from typing import Union
        Union[类型1， 。。。， 类型N]
"""
import json
import random

#  对基础类型注解
var_1: int = 10
var_2: float = 10.1
var_3: bool = True
var_4: str = '123123'

print(var_1)
print(var_2)
print(var_3)
print(var_4)


# 对类对象类型注解
class Student:
    pass


student: Student = Student()

# 对容器类型进行注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_set: set = {1, 2, 3}
my_dict: dict = {'name': 'kevinZzzzz'}
my_str: str = 'kevinZzzzz'
# 容器类型详细注解
my_list2: list[int] = [1, 2, 3, 4]
# tuple每个元素都需要标记
my_tuple2: tuple[str, int, bool] = ('123', 123, True)
my_set2: set[int] = {1, 2, 3}
# dict需要2个类型，第一个是key第二个是value
my_dict2: dict[str, int] = {'name': 222}


# 在注释进行类型注解
var_11 = random.randint(1, 10)  # type: int
var_22 = json.loads('{"name": 123}')  # type: dict[str, int]
def func():
    return 10
var_33 = func()  # type: int

# 函数注解

def add(x: int, y: int) -> int:
    return x + y

def func(data: list) -> list:
    return data

print(add(1, 2))

from typing import Union
my_list: list[Union[str, int]] = [1, 2, 'ahahahah']
my_dict: dict[str, Union[str, int]] = {"name": "KevinZzzz", "age": 29}

def func(data: Union[int, str]) -> Union[int, str]:
    pass

func()  # def func(data: int | str) -> int | str





