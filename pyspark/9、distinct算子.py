"""
    distinct算子
        功能： 对RDD数据进行去重，并返回新的RDD对象
        rdd.distinct() 无需传参
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "/usr/local/bin/python3.10"
conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 2, 4, 3, 5, 3, 4, 6])
rdd2 = rdd.distinct()
print(rdd2.collect())
