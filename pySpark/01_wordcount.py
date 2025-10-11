from typing import Any
from pyspark import RDD
from pySpark.spark_context_manager import spark_session


def reduceByKey(rdd):
    res = rdd.reduceByKey(lambda x, y: x + y)
    print(f"\n=== reduceByKey 结果 ===\n{res.collect()}")
    return res


def foldByKey(rdd: RDD[tuple[Any, int]]):
    res = rdd.foldByKey(0, lambda acc, curr: (acc + curr))
    print(f"\n=== foldByKey 结果 ===\n{res.collect()}")
    return res


def combineByKey(rdd: RDD[tuple[Any, int]]):
    res = rdd.combineByKey(
        lambda x: 1
        , lambda sum, y: sum + 1
        , lambda x, y: x + y
    )
    print(f"\n=== combineByKey 结果 ===\n{res.collect()}")
    return res


def aggregateByKey(rdd: RDD[tuple[Any, int]]):
    res = rdd.aggregateByKey(0
                             , lambda acc, curr: (acc + 1)
                             , lambda acc1, acc2: acc1 + acc2
                             )
    print(f"\n=== aggregateByKey 结果 ===\n{res.collect()}")
    return res


if __name__ == '__main__':
    with spark_session() as (ss, sc):
        list_1 = ['a m c', 'c m', 'd a', 'r r', 'a', 'd', 'a']
        rdd_1 = sc.parallelize(list_1)
        rdd_2 = sc.textFile("../data/words.txt")

        print(f"rdd_1 :\n{rdd_1.collect()}")
        print(f"rdd_2 :\n{rdd_2.collect()}")

        mappedRdd: RDD[tuple[Any, int]] = rdd_1.flatMap(lambda e: e.split(" ")) \
            .map(lambda x: (x, 1))
        mappedRdd2: RDD[tuple[Any, int]] = rdd_2.flatMap(lambda e: e.split(" ")) \
            .map(lambda x: (x, 1))
        rdd = reduceByKey(mappedRdd)
        rdd = foldByKey(mappedRdd)
        rdd = aggregateByKey(mappedRdd2)
        rdd = combineByKey(mappedRdd2)
