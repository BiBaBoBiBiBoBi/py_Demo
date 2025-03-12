"""
闭包 ： 本质， 内存函数对外层函数的局部变量的使用，此时内层函数被称为闭包函数
    可以让 一个变量常驻于内存
    可以避免全局变量被修改
      在全局操控局部变量（局部变量不容易被修改

"""
# def func():
#     a = 10
#     def inner():
#         nonlocal a
#         a+=1
#         print(a)
#         return a
#     return inner
#
# ret=func()
#
# r1 = ret()
# r2 = ret()
# print(r1,r2)

"""
装饰器  -->  要求记住结论
    本质是一个闭包（内层函数对外层函数的变量进行引用
    作用：
        在不改变函数调用的情况下，给函数增加功能
            可以在函数前后添加新功能，但是不改原来的代码
    通用装饰器的写法：
    def wrapper(fn):
        def inner(*args,**kwargs):
            # do sth before fn
            ret = fn(*args,**kwargs)  # 目标函数的执行，可以拿到返回值
            # do sth after fn
            return ret
        return inner
    
    @wrapper
    def target():
        pass
    
    一个函数被多个装饰器装饰：
    @wrapper1
    @wrapper2
    def target():
        print("i am target.")

    规律： WRAPPER1(WRAPPER2(TARGET))
    
"""
# def butler(func_game):
#     def inner(*args,**kwargs): # args -> tuple, kwargs -> dict
#         print("use cheat")
#         ret = func_game(*args,**kwargs) # 把args, kwargs 打散了，一个个传进去
#         print("close cheat")
#         return ret
#     return inner
#
# @butler
# def play_wow(username,pwd,site,role):
#     print("大地母亲忽悠着你",username,pwd,site,role)
#     return "影之哀伤"
#
# @butler
# def play_black_myth_Wukong(username,pwd):
#     print("吃俺老孙一棒！",username,pwd)
# print(play_wow("wang","goudan111","暴风之巅","心灵诅咒"))
# play_black_myth_Wukong("masterchaose","132875648")


# def wrapper1(fn):
#     def inner(*args,**kwargs):
#         print("wrapper1 in")
#         ret = fn(*args,**kwargs)
#         print("wrapper1 out")
#         return ret
#     return inner
# def wrapper2(fn):
#     def inner(*args,**kwargs):
#         print("wrapper2 in")
#         ret = fn(*args,**kwargs)
#         print("wrapper2 out")
#         return ret
#     return inner
#
# @wrapper1
# @wrapper2
# def target():
#     print("i am target.")

# target() #  WRAPPER1(WRAPPER2(TARGET))


"""

"""
login_flag = False


def verify_user_info(fn):
    def inner(*args, **kwargs):
        global login_flag
        if login_flag == False:
            while 1:
                print(":plz input user name and pwd...")
                username = input("username>>>")
                pwd = input("pwd>>>")
                if pwd == '123' and username == "admin":
                    print("log in success!")
                    login_flag = True
                    break
                else:
                    print("incorrect info!")

        ret = fn(*args, **kwargs)
        return ret

    return inner

@verify_user_info
def add_op():
    print("add op done.")

@verify_user_info
def del_op():
    print("del op done.")

@verify_user_info
def update_op():
    print("update op done.")

@verify_user_info
def search_op():
    print("search op done.")

del_op()
search_op()