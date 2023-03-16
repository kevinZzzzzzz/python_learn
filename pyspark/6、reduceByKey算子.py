"""
reduceByKey算子
    功能：针对KV型RDD，自动按照key分组，然后根据你提供的聚合逻辑，完成组内数据value的聚合操作
    KV型： 二元元组(key, value)

    rdd.reduceByKey(func)
    funcL (v,v) -> v
    接收两个传入参数（类型要一致），自动按照key分组，返回一个返回值，类型和传入要求一致
"""
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "/usr/local/bin/python3.10"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([('男', 1), ('男', 2), ('女', 2), ('女', 1), ('女', 3)])
rdd2 = rdd.reduceByKey(lambda x, y: x + y)


print(rdd2.collect())