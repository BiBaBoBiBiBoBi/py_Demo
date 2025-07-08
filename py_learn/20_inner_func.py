"""
匿名函数：
    lambda表达式
        var = lambda x,y:x+y

"""
# sum_of_two_num = (lambda x,y:x+y)(2,3)
# pow_of_two = lambda x,y:x**y
# print(pow_of_two(2,3))
# print(sum_of_two_num)


"""
zip
    将多个可迭代内容进行合并, 以最短的迭代对象为标准
"""
# lst_1 = ['a','b','c','d','e']
# lst_2 = ['b','c','d','e','f']
# lst_3 =[40,20,11]
#
# result_zip = zip(lst_1,lst_2,lst_3)
# lst_zip=list(result_zip)
# print(lst_zip)  #   [('a', 'b', 40), ('b', 'c', 20), ('c', 'd', 11)]
# for e in result_zip:
#     print(e)
# for a, b, c in lst_zip: # 拆包
#     print(f"a:{a}, b:{b}, c:{c}")


"""
locals() 以词典类型返回当前所在作用域的全部局部变量
globals()  以词典类型返回 全部局部变量
"""
test_loc = 'iam local'
# print(locals()) # 打印全域的所有内容
# def func_local():
#     a=789
#     print(locals())  # 打印当前局部域的所有内容
#     print(globals())
# func_local()

"""
sorted(obj,key = 排序函数 , reverse= bool )
    排序
"""
# lst = [2, 3, 7, 3, 6, 12, 9, 4]
# s = sorted(lst)
# s_r = sorted(lst, reverse=True)  # 倒序排列
# print(s, s_r)

# lst_str = ["王", "lee2", "品阿萨", "王怕"]
# print(sorted(lst_str))
# def sort_func(str):
#     return len(str)
# lst_sorted=sorted(lst_str,key=sort_func,reverse=False)
# lst_sorted = sorted(lst_str, key=lambda x: len(x), reverse=False)
# print(lst_sorted)
# lst = [
#     {"id": 1, "name": "zhou ng", "age": 42, "salary": 12555}
#     , {"id": 2, "name": "wu xcy", "age": 12, "salary": 7633}
#     , {"id": 3, "name": "zhang jmm", "age": 33, "salary": 6533}
#     , {"id": 4, "name": "zhaao gy", "age": 53, "salary": 5634}
#     , {"id": 5, "name": "xiao hh", "age": 35, "salary": 2345}
# ]
# lst_sorted = sorted(lst,key = lambda x:x["age"] , reverse=True)
# print(lst_sorted)

"""
filter

"""
# lst_str = ["王", "lee2", "品阿萨", "王怕","王大胆","刘琴青"]
# f = filter(lambda s:not s.startswith("王"),lst_str) # 是一个生成器，需要用List组装
# print(list(f))

"""
map

"""
lst = [2, 3, 7, 3, 6, 12, 9, 4]
r = map(lambda i: (i ** 2, 1), lst)
print(dict(r)) # 是一个生成器，需要用dict组装
