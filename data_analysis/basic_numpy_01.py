"""
提出问题
准备数据
分析（清洗）数据

必学模块
    numpy
    pandas（数据清洗
    matplotlib（可视化*
    pyecharts(进阶可视化
"""

"""
numpy
做科学计算，重在数值计算  【是数组】 可以类比成python的列表

    - array
    numpy.array 通常比 list 使用更少的内存，因为它存储的是**同质类型**的数据。
    list 由于存储的是对象引用，可能会使用更多的内存。
    
    numpy.array 提供了大量的数学和统计函数，可以进行高效的数组运算，如矩阵乘法、傅里叶变换等。
    list 没有内置的数值计算功能，需要借助其他库（如 math 或 numpy）来实现。
    
    numpy.array 的切片操作返回的是数组的视图（view），对视图的修改会反映到原数组上。
    list 的切片操作返回的是列表的副本（copy），修改副本不会影响原列表。
    
    numpy.array 支持多维数组（如矩阵和张量），这是 list 不直接支持的。
    list 可以通过嵌套列表来模拟多维数组，但这通常不如 numpy.array 方便和高效。
"""
import numpy as np
'''
数学和统计方法
np.sum(array, axis)：计算数组的总和。
np.mean(array, axis)：计算数组的均值。
np.std(array, axis)：计算数组的标准差。
np.var(array, axis)：计算数组的方差。
np.min(array, axis) / np.max(array, axis)：计算数组的最小值/最大值。
np.median(array, axis)：计算数组的中位数。
np.percentile(array, q, axis)：计算数组的百分位数。

布尔和比较操作
array == value：逐元素比较数组和值是否相等。
array > value：逐元素比较数组中的元素是否大于给定值。
np.logical_and(array1, array2)：逐元素逻辑与操作。
np.logical_or(array1, array2)：逐元素逻辑或操作。
'''
# create a array
arr = np.array([3, 4, 5, 6, 8, 9])
print(f"arr:{arr}")  # [3 4 5 6 8 9]
arr_2 = np.array([[6, 5, 3], [6, 4, 9]])
print(f"np.arange(10) = {np.arange(10)}") # [0 1 2 3 4 5 6 7 8 9]
print(f"np.arange(0,10,2) = {np.arange(0,10,2)}")
print(np.array(range(0,10,2)))
# print(arr_2)  # [[6 5 3]
# [6 4 9]]
# print(arr_2[1][0]) # arr_2[1] -> lst[6,4,9] ,arr_2[1][0] -> 6

''' arr batch operate '''
lst = list(i + 1 for i in arr)
print(f"lst = arr + 1 : {lst}")
# equals
arr += 1
print(f"arr + 1 : {arr}")
print(f"arr[1:3] = {arr[1:3]}")

'''
随机数生成
np.random.rand(d0, d1, ..., dn)：生成 [0, 1) 之间的随机数。
np.random.randn(d0, d1, ..., dn)：生成标准正态分布的随机数。
np.random.randint(low, high, size)：生成指定范围内的随机整数。 size 是生产个数或者维度，size =3 / size = (3,4) 
'''
rand_num = np.random.randint(19,29,3) # rand(row , col ) 多维随机数组 [0，1)
print(f"random = {rand_num}")
