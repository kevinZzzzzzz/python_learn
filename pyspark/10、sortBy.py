"""
sortBy算子
    对RDD数据进行排序，基于你指定的排序依据
    rdd.sortBy(func, ascending=False, numPartitions=1)
    func：(T) -> U 告知rdd中的哪个数据进行排序
    ascending True升序 False降序
    numPartitions：用多少分区排序
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "/usr/local/bin/python3.10"
conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
sc = SparkContext(conf=conf)

rdd = sc.textFile('./hello2.txt')
word_rdd = rdd.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
print(word_rdd.collect())

# 对数据按数量大小进行排序
sort_rdd = word_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print(sort_rdd.collect())
