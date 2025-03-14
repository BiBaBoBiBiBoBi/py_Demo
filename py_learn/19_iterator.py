"""
可迭代的数据类型都会提供迭代器，他可以帮我们把数据类型中的所有数据逐一地拿到

获取迭代器的两种方案：
    1 .iter()
    2 . __iter()__

从迭代器中拿到数据
    1.next()函数
    2 __next()__ 特殊方法

总结： 迭代器同意了所有不同的数据类型 有了相同的遍历方式
    只能向前，不能往后
    一次性的
    特别省内存（只存一个指针
    惰性机制
"""

# it=iter("鸟礁名字")
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
#
# it2 = "hehehe".__iter__()
# print(it2.__next__())
# print(it2.__next__())
# print(it2.__next__())

"""
生成器：
    生成器的本质就是迭代器
    创建方案
        1 生成器函数
            生成器函数关键字 yield
            生成器函数执行的时候，并不会执行函数，得到的是生成器
            
            yield:只要函数中出险了yield，他就是生成器函数
                作用：
                    1 可以返回数据
                    2 可以分段执行函数,通过__next()__ 可以执行到下一个yield之前的函数
                优势：用好了，很节省内存
                
        2 生成器表达式 
            语法： (数据 for循环 if)
        节省内存
        
"""


# def func():
#     print(123)
#     yield 999
#     print(312)
#     yield 888
#
# ret=func()
# print(ret.__next__()) # 只有执行到next的时候参会返回数据
# print(ret.__next__()) # 执行第二段，如果没有就返回stop iteration

# 1 生成器函数
def order():
    lst = []
    for i in range(40):
        lst.append(f"cloth-{i}")
        if len(lst) == 10:
            yield lst  # <==> stop and return lst
            # 截断函数，下一次从这里继续拿数据
            lst = []


gen_order = order()
''' 1 for 最方便'''
# for i in gen_order:
#     print(i)

''' 2 while需要手动检查'''
while True:
    batch = next(gen_order, None)  # 如果生成器耗尽，返回 None
    if batch is None:
        break
    print(batch)

# print(gen_order.__next__())
# print(gen_order.__next__())
# print(gen_order.__next__())
# print(gen_order.__next__())

"""
推导式：
    简化代码。
    语法：
        列表推导式：[数据 for循环 （if判断）]
"""
# lst_01 = [i for i in range(1,11,2)]
# lst_01 = [i for i in range(1,10) if i % 2 ==1]
# lst_02 = [f"cloth+{i}" for i in range(10)]
# print(lst_01)
# print(lst_02)
# lst_03=["allen","lily","lee"]
# lst_04=[e.upper() for e in lst_03]
# print(lst_04)
# sum=(lambda x,y:x+y)(1,3)
# print(sum)
"""集合推导式"""
s = {i for i in range(10)}
"""字典推导式"""
lst_03 = ["a", "v", "l", "r", "f"]
# s = {i: lst_03[i] for i in range(len(lst_03))}
s = {ind: val for ind, val in enumerate(lst_03)}  # {0: 'a', 1: 'v', 2: 'l', 3: 'r', 4: 'f'}
print(s)
"""
2 生成器表达式  (数据 for循环 if)
"""
gen = (i ** 2 for i in range(6))
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
for item in gen:
    print(item)
"""生成器是一次性的，本质是迭代器"""
lst_04 = list(gen)  # lst_04 = [i for i in gen]
print(lst_04)
# lst_s = list("iamagoodperson") # list中一定有迭代循环的过程 list-> for -> next()
# print(lst_s)
