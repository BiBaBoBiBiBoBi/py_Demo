def calculate_sector(c1, r1):
    area = c1 / 360 * 3.14 * r1 ** 2
    return area


def calculate_BMI(weight, height):
    user_BMI = float(weight) / (float(height) ** 2)
    return user_BMI

# // 代表向下取整
def getMedianOfList(num_list):
    sort_lst = sorted(num_list)
    n = len(num_list)
    if n % 2 == 1:
        return sort_lst[n // 2]
    else:
        half = sort_lst[int(n/2)] + sort_lst[int(n/2) - 1]
        return half / 2


print(calculate_sector(160, 3))
print(calculate_BMI(76, 1.79))

lst = [1, 2, 3, 4, -3, 9, 23, -5 - 6]
print(sum(lst))

from statistics import median
print(median(lst))
print(getMedianOfList(lst))

# import model
# 1 import model_name
# 2 from model_name import func1,func2
# 3(un suggested) from model_name import * ;( it will import all the variables and func and maybe cause some bugs)

