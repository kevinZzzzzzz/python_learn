"""
map算子
    将RDD的数据一条条处理，处理的逻辑是基于map中接收的处理函数，返回新的RDD对象
"""
from pyspark import SparkConf, SparkContext

import os
os.environ['PYSPARK_PYTHON'] = "/usr/local/bin/python3.10"
conf = SparkConf().setMaster('local[*]').setAppName('text_spark')
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])
# (T) -> U 接收传入一个参数类型 返回一个类型
def func(data):
    return data * 10
rdd2 = rdd.map(func)
#
print(rdd2.collect())

# sc.stop()
