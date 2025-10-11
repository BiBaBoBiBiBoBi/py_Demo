from typing import Any

from pySpark.spark_context_manager import spark_session

def fun_reduce(nums)-> tuple[Any, Any]:
    rdd_1 = sc.parallelize(nums)
    rdd_avg = rdd_1.map(lambda x: (x, 1)) \
        .reduce(lambda acc, curr: (acc[0] + curr[0], acc[1] + curr[1]))
    # avg = rdd_avg[0] / rdd_avg[1]
    return rdd_avg[0], rdd_avg[1]

# seqOp：对每个分区中的元素进行累加
    # combOp：合并不同分区的累加结果
def seqOp(acc, x):
        return (acc[0] + x, acc[1] + 1)

def combOp(acc1, acc2):
        return (acc1[0] + acc2[0], acc1[1] + acc2[1])

def fun_aggregate(nums)-> tuple[int, int]:
    rdd_1 = sc.parallelize(nums)
    zero_value=(0,0)
    sum,count = rdd_1.aggregate(zero_value
                    ,lambda acc,x:(acc[0] + x, acc[1] + 1) # 分区内累加
                    ,lambda acc1,acc2:(acc1[0] + acc2[0], acc1[1] + acc2[1]) # 分区之间累加
                    )
    # sum,count = rdd_1.aggregate(zero_value,seqOp,combOp)
    return sum,count

def fun_useDataFrame(nums):
    df = ss.createDataFrame([(x,) for x in nums], ["value"])
    df.selectExpr("avg(value) as average").show()

def fun_fold(nums):
    rdd_1=sc.parallelize(nums)
    fold_tuple = rdd_1.map(lambda x:(x,1)) \
        .fold((0,0),lambda acc,curr:(acc[0]+curr[0] , acc[1]+curr[1]))
    return fold_tuple

if __name__ == '__main__':
    with spark_session() as (ss,sc):
        nums = [1, 2, 3, 4, 6, 8, 2, 5, 7, 8]
        # avg_tuple = fun_reduce(nums)
        # avg_tuple = fun_aggregate(nums)
        fun_useDataFrame(nums)
        avg_tuple = fun_fold(nums)
        print(f"总和: {avg_tuple[0]}, 总个数: {avg_tuple[1]}, 平均数: {avg_tuple[0]/avg_tuple[1]}")
