# 转义字符
# print("Hello,\'  \'  \"  \\ World!")

# 换行
# print("Hello,\n World!")

# 三引号
# print(''' u can print anything here without using \\n instead of \'\'\' ''')

#字符串前面的 r 或 R 表示这是一个原始字符串（raw string）。原始字符串是一种特殊的字符串，它不会对反斜杠 \ 进行转义处理
file_path = r'C:\Users\Name'
#需要注意的是，原始字符串仍然会对其他特殊字符（如单引号、双引号等）进行转义处理，只是不会对反斜杠进行转义处理。
s1 = r'He said, "Hello, World!"'  # 双引号会被转义
s2 = r"He said, 'Hello, World!'"  # 单引号会被转义
# print(s1,s2,sep='|')

# variables
my_name = "Jeremy"

# 2**3 <=> 2^3
res_01 = 2 ** 3  # =8
res_02 = 8 /9  #0.888888
res_floor = 8 // 9 # 0  向下取整
print(f"res2 = {res_02} , res_floor = {res_floor}")
import math
res_02 = math.pow(2, 3)

# calulate equation : a,b,c
a = 1
b = 9
c = 20
# res_eq_01 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
# res_eq_02 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
# need to use func 'str()' to trans type-float  to string
# ,or it will go wrong:TypeError: can only concatenate str (not "float") to str
# print("res = " + str(res_eq_01) + "  //  " + str(res_eq_02))

# 进制转换
# a =19
# a_b = bin(a)
# a_o=oct(a)
# a_x=hex(a)
# a_int = int(a_o)

# sum min max pow

# list
# s= {1,2,3,}
# lst_1= list(s)
# lst_2 = list("ajiiwjk") #['a', 'j', 'i', 'i', 'w', 'j', 'k']
# lst_2.reverse()
# print(lst_2)

# slice
sli = slice(1,4,2) # [1,4,2]
# print("abc1234567"[sli])  #->  b1

# ord  chr
# py的内存中是unicode编码
# a = "中"
# print(ord(a)) #  中字的码位20013
# print(chr(20013)) #  中
# 655536个字，最多..
# for i in range(65536):
    # print(chr(i)+" ",end ='') # 打印所有字符
    # pass

# dict set frozenset，后俩不可变
dic={"a":1,"s":33}
# set =set((a,c1,23))
sett=frozenset((1,2,3,4))
# len sorted enumerate  all any  zip  filter  map
# print(all([0,"",'都得'])) # all  ==  and   0 and "" and '都得'
# print(any([1,"",''])) # equals  -->  or

lst_02= ["aa","vv","cc","dd"]
# for e in enumerate(lst_02):
#     print(e)
'''解包 ind,e '''
# for ind,e in enumerate(lst_02):
#     print(ind,e)
'''
(0, 'aa')
(1, 'vv')
(2, 'cc')
(3, 'dd')
'''
# # enumerate 等价于
# for i in range(len(lst_02)):
#     print(i,lst_02[i])

# 打印对象的操作方法
# print(dir(dic))