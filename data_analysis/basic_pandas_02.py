'''
series , 可以当成表格中的行或者列
dataframe , 数据表格
    df 是由 series 组成
'''
def minus(x,*args):
    sum1 = sum(args)
    return x - sum1

print(minus(1,2,3,4,5))

