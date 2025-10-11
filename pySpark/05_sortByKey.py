from spark_context_manager import spark_session


if __name__ == '__main__':
    with spark_session() as (ss,sc):
        rdd_1 = sc.textFile("../data/words.txt")
        wordCountRdd = rdd_1.flatMap(lambda x: x.split(' ')) \
            .map(lambda x:(x,1)) \
            .reduceByKey(lambda x,y:(x+y))

        print(f"wcRdd:{wordCountRdd.collect()}")
        print(f"{wordCountRdd.count()}")
        print(f"===========sortByKey======================")
        print(f"{wordCountRdd.sortByKey().collect()}")
        print(f"{wordCountRdd.sortByKey(False).collect()}")

        # 求和
        print(f"===========sum======================")
        numbers = sc.parallelize([1, 2, 3, 4])
        sum = numbers.fold(0, (lambda x, y: x + y))
        print(f"{sum}")

        print(f"===========sortByValue======================")
        sortByValue = wordCountRdd.sortBy(lambda x:x[1], ascending=False)
        print(f"{sortByValue.collect()}")
