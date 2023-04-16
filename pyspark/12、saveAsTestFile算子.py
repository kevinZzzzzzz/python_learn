"""
saveAsTextFile算子
    功能：将RDD的数据写入文本文件中
    支持本地写出，hdfs等文件系统

    修改rdd分区为1个
        方法1、SparkConf对象设置属性全局并行度为1：
            conf.set('spark.default.parallelism', 1)
        方法2、创建rdd对象的时候设置parallelize方法传入numSlices参数为1
"""
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "/usr/local/bin/python3.10"
os.environ['HADOOP_HOME'] = '/users/kevinzzzzzz/hadoop-3.3.4/bin/hadoop'
conf = SparkConf().setMaster('local[*]').setAppName('text_spark')
conf.set('spark.default.parallelism', 1)
sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([1, 2, 3, 4, 5, 6], numSlices=1)
rdd1.saveAsTextFile('./output1.txt')

# rdd2 = sc.parallelize([('hello', 3), ('spark', 5), ('h1', 7)])
# rdd2.saveAsTextFile('../output2.txt')
# rdd3 = sc.parallelize([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# rdd3.saveAsTe xtFile('../output3.txt')
