"""
 filter算子
    功能；过滤出想要的数据
    func：（T）=> bool 传入1个参数进来随意类型，返回值必须是true or false
"""

from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "/usr/local/bin/python3.10"
conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = rdd.filter(lambda num: num % 2 == 0)
print(rdd2.collect())