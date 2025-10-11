import findspark
from typing import Generator, Tuple
from pyspark import SparkContext
from pyspark.python.pyspark.shell import sqlContext

findspark.init()  # 自动配置 SPARK_HOME，解决 Windows/IDE 环境问题

from pyspark.sql import SparkSession
from contextlib import contextmanager


@contextmanager
def spark_session(app_name="MyApp", master="local[1]") -> Generator[Tuple[SparkSession, SparkContext], None, None]:
    """上下文管理器：自动创建和关闭 SparkSession"""
    import os
    os.environ['PYSPARK_PYTHON'] = r'C:\Users\goudan\.conda\envs\py_Demo\python.exe'
    os.environ['PYSPARK_DRIVER_PYTHON'] = r'C:\Users\goudan\.conda\envs\py_Demo\python.exe'
    active_session = SparkSession.getActiveSession()
    if active_session is not None:
        print("⚠️ 警告：检测到已经有一个活动的 SparkSession！请确保这是第一次初始化 Spark！")
        active_session.stop()
    else:
        print("✅ 当前没有活动的 SparkSession，可以安全初始化。")

    ss = SparkSession.builder \
        .appName(app_name) \
        .master(master) \
        .getOrCreate()
    sc = ss.sparkContext
    # from pyspark.sql import SQLContext
    # sqlContext = SQLContext(sc)
    print("✅ Spark 已初始化！")
    print("SparkSession:", ss)
    print("SparkContext:", sc)
    try:
        yield ss, sc  # 在此 yield 之后的代码块中可以使用 spark
    finally:
        print("正在关闭 SparkSession...")
        ss.stop()
        print("SparkSession 已关闭")

# 如果不使用 @contextmanager，得这么写（功能一样，但更冗长）：
# class SparkSessionManager:
#     def __init__(self, app_name, master):
#         self.app_name = app_name
#         self.master = master
#         self.ss = None
#         self.sc = None
#
#     def __enter__(self):
#         self.ss = SparkSession.builder \
#             .appName(self.app_name) \
#             .master(self.master) \
#             .getOrCreate()
#         self.sc = self.ss.sparkContext
#         return self.ss, self.sc
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("正在关闭 SparkSession...")
#         self.ss.stop()
#         print("SparkSession 已关闭")

# 使用时
#     with SparkSessionManager("MyApp", "local[2]") as (ss, sc):
#         ...
