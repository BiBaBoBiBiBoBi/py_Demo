from spark_context_manager import spark_session
from pyspark.sql import SparkSession

if __name__ == '__main__':
    with spark_session() as (ss, sc):
        r = sc.textFile("../data/R.txt")
        print(r.collect())

        s = sc.textFile("../data/S.txt")
        print(s.collect())

        r1 = r.map(lambda x: x.split(",")).flatMap(lambda s: [(s[0], s[1])])
        # print(f"r1:\n{r1.collect}")
        s1 = s.map(lambda x: x.split(",")).flatMap(lambda s: [(s[0], s[1])])

        joinedRdd = r1.leftOuterJoin(s1)  # joinedRdd=r1.join(s1)
        print(joinedRdd.collect())
        # [('k1', ('v1', 'v11')),
        #  ('k1', ('v1', 'v22')),
        #  ('k1', ('v1', 'v33')),
        #  ('k1', ('v2', 'v11')),
        #  ('k1', ('v2', 'v22')),
        #  ('k1', ('v2', 'v33')),
        #  ('k2', ('v3', 'v55')),
        #  ('k2', ('v4', 'v55')),
        #  ('k3', ('v7', None)),
        #  ('k3', ('v8', None)),
        #  ('k3', ('v9', None))]

        unionRdd = r1.union(s1)
        print(f"union:\n{unionRdd.collect()}")
        # [('k1', 'v1'), ('k1', 'v2'), ('k2', 'v3'), ('k2', 'v4'), ('k3', 'v7'), ('k3', 'v8'), ('k3', 'v9'), ('k1', 'v11'), ('k1', 'v22'), ('k1', 'v33'), ('k2', 'v55'), ('k4', 'v77'), ('k5', 'v88')]
        # 和下面等价 ：unionRdd.flatMap(lambda t:[t[0],t[1]])
        res = unionRdd.flatMap(lambda t:t) \
            .map(lambda x: (x, 1)) \
            .foldByKey(0, lambda acc, curr: acc + curr)
        print(f"res:\n{res.collect()}")