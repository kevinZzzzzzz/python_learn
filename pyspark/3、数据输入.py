"""
RDD全称为弹性分布式数据集
PySpark针对数据的处理都是以RDD对象作为载体
    数据存储在RDD内
    各类数据的计算方法都是RDD对象
    RDD的数据计算方法，返回值依旧是RDD对象


数据容器转RDD对象
SparkContext对象的parallelize()
"""

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local[*]').setAppName('text_spark')
sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([1, 2, 3, 4])  # [1, 2, 3, 4]
rdd2 = sc.parallelize((1, 2, 3, 4))  # [1, 2, 3, 4]
rdd3 = sc.parallelize('aadasdasd')  # ['a', 'a', 'd', 'a', 's', 'd', 'a', 's', 'd']
rdd4 = sc.parallelize({1, 2, 3, 4})  # [1, 2, 3, 4]
rdd5 = sc.parallelize({"key1": "value1", "key2": "value2"})  # ['key1', 'key2']

# 查看RDD内容
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())

# 读取文件转RDD对象
rdd5 = sc.textFile('./hello.txt')
print(rdd5.collect())  # ['hahahaha', 'haheheheh', 'kevinZzzz', 'shdasd ', 'sfqwrqw']

sc.stop()
