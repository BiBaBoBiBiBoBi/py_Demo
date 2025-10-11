import findspark
from pyspark.python.pyspark.shell import sqlContext

findspark.init()  # 自动配置 SPARK_HOME，解决 Windows/IDE 环境问题

# 创建 SparkSession 和 SparkContext
# 创建一个全局的 SparkSession（通常命名为 ss 或 spark）
from pyspark.sql import SparkSession


ss = SparkSession.builder \
    .appName("spark app") \
    .master("local[1]") \
    .getOrCreate()

# 获取 SparkContext
sc = ss.sparkContext
# from pyspark.sql import SQLContext
# sqlContext = SQLContext(sc)
# 打印初始化信息（调试用）
print("✅ Spark 已初始化！")
print("SparkSession:", ss)
print("SparkContext:", sc)
