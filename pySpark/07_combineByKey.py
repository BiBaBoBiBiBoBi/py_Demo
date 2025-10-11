from init_spark import ss, sc


def main():
    # 原始输入数据：一系列 (key, value) 键值对
    input = [
        ("k1", 1), ("k1", 2), ("k1", 3), ("k1", 4), ("k1", 5),
        ("k2", 6), ("k2", 7), ("k2", 8),
        ("k3", 10), ("k3", 12)
    ]

    # 创建 RDD
    rdd = sc.parallelize(input)

    # -------------------------------
    # 使用 combineByKey 进行聚合：
    # 目标：对每个 key，计算 value 的总和 与 计数（即 sum 和 count）
    # -------------------------------
    sumRdd = rdd.combineByKey(
        lambda x: (x, 1)
        , lambda sum, cur: (sum[0] + cur, sum[1] + 1)
        , lambda x, y: (x[0] + y[0], x[1] + y[1])
    )

    # 打印每个 key 的 (sum, count)
    print("每个 key 的总和与计数:")
    print(sumRdd.collect())
    # 输出类似：[('k3', (22, 2)), ('k2', (21, 3)), ('k1', (15, 5))]

    # -------------------------------
    # 计算平均值：对每个 key，用 sum / count
    # -------------------------------
    avg = sumRdd.mapValues(lambda v: v[0] / v[1])

    # 打印每个 key 的平均值
    print("\n每个 key 的平均值:")
    print(avg.collect())
    # 输出类似：[('k3', 11), ('k2', 7), ('k1', 3)]


if __name__ == '__main__':
    try:
        main()
    finally:
        ss.stop()
