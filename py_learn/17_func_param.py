"""
参数：
    1 位置参数 ( 按照位置进行传递的参数
    2 默认值参数 （ 缺省就按默认值，不缺省按传入值
    3 动态传参
        1 *args 表示接收所有的位置参数的动态传参  -> tuple
        2 **kwargs 表示接受所有的关键字的动态传参  ->  dict
    4 关键字参数
        按照参数的名字进行传参 （ para_name = 'value' )

    顺序*： 位置 > *args > 默认值 > **kwargs

"""
from typing import List


def record(name, age, gender='male'):
    print(name, age, gender)


def eat(*food, **desert):
    print(type(food), food, sep='\n')
    print(type(desert), desert, sep='\n')


def func_print1(*args):
    print(args)
    return args  # --> tuple


def func_print2(**args):
    print(args)


def twoSum(nums: List[int], target: int) -> List[int]:
    map = {}
    for i in range(len(nums)):
        other = target - nums[i]
        if other in map:
            print([i, map[other]])
            return [i, map[other]]
        map[nums[i]] = i


if __name__ == '__main__':
    # record("na", 12)
    # record("ka", 34, "female")
    # eat("1", 23, 'asf', 'ooo', a=123, m='oks')

    # record("na", 12)
    # record("ka", 34, "female")

    # stu_lst = ['mark','lee','john','joe']
    # stu_dict={'a':1,'v':3}
    # func_res = func_print1(*stu_lst)   # *在实参位置，把列表打散成位置参数进行传递
    # func_print2(**stu_dict) # **在实参位置，把字典打散成位置参数进行传递
    #
    # print(type(func_res),func_res)

    twoSum(nums=[1, 3, 4, 2], target=6)
