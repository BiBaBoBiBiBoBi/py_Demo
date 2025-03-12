"""
可迭代的数据类型都会提供迭代器，他可以帮我们把数据类型中的所有数据逐一地拿到

获取迭代器的两种方案：
    1 .iter()
    2 . __iter()__

从迭代器中拿到数据
    1.next()函数
    2 __next()__ 特殊方法

总结： 迭代器同意了所有不同的数据类型 有了相同的遍历方式
"""

it=iter("鸟礁沙名字")
print(next(it))
print(next(it))
print(next(it))
print(next(it))

it2 = "hehehe".__iter__()
print(it2.__next__())
print(it2.__next__())
print(it2.__next__())
