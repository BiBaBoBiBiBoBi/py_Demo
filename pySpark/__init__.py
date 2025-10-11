# 当有人导入这个包时，自动初始化 Spark（可选）
# 如果你希望一导入包就初始化 Spark，可以在这里导入 spark_init
# 但更推荐“按需导入”，见后面的使用方式

# 【可选】：如果你希望包一被导入就初始化 Spark，可以取消下面两行的注释
# from .init_spark import ss, sc  # 导入全局的 SparkSession 和 SparkContext
# print("🔥 my_spark_project 包已加载，并初始化 Spark")