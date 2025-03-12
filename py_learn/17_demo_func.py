# 高阶函数 ，函数作为参数的函数
#  匿名函数 lambda
        # lambda n1, n2 : n1 + n2   ( 关键字，参数，函数返回表达式，冒号后面只能有一个语句/表达式
# 直接调用匿名函数

#  python 编程 入门到实践（第三版） eric matthes
# 数据分析， AI
res1 = (lambda n1,n2: n1 ** n2 -55)(2,3)
# print(res1)

# Python with spark
# Python with pandas              Data op and analysis
# Python with ai


# 深浅拷贝
# 浅拷贝：复制对象的引用，修改会同步变化。（指向相同的内存地址
list=[1,2,3,[55,3,2],9]
l1=list
l1.append(7)
# print("list",list,sep=' ',end='...\n')
# # 查看内存地址 id()
# print(id(list),id(l1),sep='\n')
# print("=============")
import copy
l2 = copy.copy(list) # 但如果是嵌套列表， 外层数据结构的地址不同，
l2.append(888)
# print("list and l2:",list,l2,sep='\n')
# print(id(list),id(l2),sep='\n')
# #但是内层数据结构任然是同一地址
# print("INNER list and l2:",id(list[3]),id(l2[3]),sep='\n')

# print("=============")
# 深拷贝
deep_list = copy.deepcopy(list)
# print("deep list and list",id(list),id(deep_list),sep='\n')
list[3].append(1011)
# print(list,deep_list)
# 内层数据的地址也不同
# print("INNER: deep list and list",id(list[3]),id(deep_list[3]),sep='\n')

# 递归
def recursion_func():
    if 3>2:
        return
    func()
    pass

"""
作用域
"""
c = 100 # ’顶格‘声明的变量或者函数 处于 全局作用域 / 或者在main中


"""
函数嵌套
"""
# def func01():
#     b=20
#     def func03():
#         pass
#         def func04():
#             print(123123)
#         func04()
#     func03() # 局部的东西，一般都是局部自己访问使用
#     print(123)

# def func02():
#     def inner_func():
#         print("inner123")
#         pass
#     print(inner_func)
#     return inner_func
"""return a function,cant add '()',cause if u do,u will execute func rather than return it"""
#
# b1 = func02()# b1 = inner_func
# b1()
#
# # 代理模式
# def fun_high(a):
#     print(a)
#     a() # 执行这个函数
#
# fun_high(b1)  # 实参可以是函数
"""
函数可以作为参数传递
    可以作为返回值
* 函数本质就是一个变量，都表示一个内存地址
"""


"""
global  在局部引入全局变量
nonlocal  在局部， 引入外层的 局部变量
    向外找一层，如有就引入，如果没有同名变量，就继续向外。直到 全局（不包括
"""
out_a = 10

def func():
    global out_a
    out_a = 12
    b =33
    def func2():
        nonlocal b
        print(b)
        b=15
    func2()
    print(b)

func()
print(out_a)

