"""
得出每个单词出现的次数 
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "/usr/local/bin/python3.10"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.textFile('./hello2.txt')
word_rdd = rdd.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1))
word_rdd2 = word_rdd.reduceByKey(lambda x, y: x + y)
print(word_rdd2.collect())


