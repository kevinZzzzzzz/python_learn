from pyspark import SparkConf, SparkContext

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName('test_spark_app')
# 基于SparkConf类对象创建SparkContext类对象
sc = SparkContext(conf=conf)
print(sc.version)

# 停止SparkContext对象的运行
sc.stop()

