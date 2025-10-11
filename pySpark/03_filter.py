from pySpark.spark_context_manager import spark_session

if __name__ == '__main__':
    with spark_session() as (ss, sc):
        numRdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7])
        print(f"nums:{numRdd.collect()}")
        filterRdd = numRdd.filter(lambda x: x % 2 == 1)
        print(filterRdd.collect())

        dataRdd = sc.parallelize([('a', 'b'), ('c', 'd', 'e'), ('f',), ('g', 'h', 'i', 'j')])
        flatRdd = dataRdd.flatMap(lambda t:t)

        print(f"{flatRdd.collect()}")
