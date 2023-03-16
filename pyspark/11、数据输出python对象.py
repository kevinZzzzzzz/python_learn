"""
数据输出python对象
    collet算子
        将RDD数据统一收集到Driver中，形成一个List对象
    reduce算子
        将rdd对象进行累加计算
    take算子
        取出RDD的前N个元素，组合成list返回给你
    countsuanz
        计算RDD内忧多少条数据
"""
"""
map算子
    1、将RDD的数据一条条处理，处理的逻辑是基于map中接收的处理函数，返回新的RDD对象
    2、只要返回值是RDD对象，就可以通过链式调用的方法多次调用算子
"""
from pyspark import SparkConf, SparkContext

# import os
# os.environ['PYSPARK_PYTHON'] = "/usr/local/bin/python3.10"
conf = SparkConf().setMaster('local[*]').setAppName('text_spark')
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])
# (T) -> U 接收传入一个参数类型 返回一个类型
rdd_list: list = rdd.collect()
print(rdd_list) # [1, 2, 3, 4, 5]
print(type(rdd_list)) # <class 'list'>


rdd2 = sc.parallelize(range(1, 11))
rdd3 = rdd2.reduce(lambda x, y: x + y)
print(rdd3) # 55

rdd4 = rdd2.take(5)
print(rdd4) # [1, 2, 3, 4, 5]

rdd5 = rdd2.count()
print(f"rdd2内有{rdd5}个元素") # 10
# sc.stop()
