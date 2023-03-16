"""
flatMap算子
    功能对RDD进行map操作，然后进行解除潜逃操作，相当于js数组的扁平化flatten
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "/usr/local/bin/python3.10"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize(['asdas asda weqw', "sdfas asdas  asdas", 'python kevinZzzzzz'])

rdd2 = rdd.map(lambda x: x.split(' '))
rdd3 = rdd.flatMap(lambda x: x.split(' '))
print(rdd2.collect())
print(rdd3.collect())

