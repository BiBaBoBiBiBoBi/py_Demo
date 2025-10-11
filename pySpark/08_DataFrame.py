from spark_context_manager import spark_session

if __name__ == '__main__':
    with spark_session() as (ss,sc):
        iphoneRDD = sc.parallelize([
            ("XS", 2018, 5.65, 2.79, 6.24),
            ("XR", 2018, 5.94, 2.98, 6.84),
            ("X10", 2017, 5.65, 2.79, 6.13),
            ("8Plus", 2017, 6.23, 3.07, 7.12)
        ])

        names = ['Model', 'Year', 'Height', 'Width', 'Weight']
        df = ss.createDataFrame(iphoneRDD, names)
        df.describe()
        df.show(3)
