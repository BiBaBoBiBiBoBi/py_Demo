import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 创建表格
workout_dict = {
    "calories" :[441,234,90],
    "duration":[50,40,34],
    "type":['run','walk','runrun']
}
workout = pd.DataFrame(workout_dict)
print(workout)
print("============================\n")
# 列索引
print(f"column : {workout.columns}\n")
workout.columns=['re-calories', 're-duration', 're-type']
print(f"renamed col : {workout.columns}\n")

# 行索引
print(f"index : {workout.index}\n")
workout.index=['day1','day2','day3']
print(f"renamed index : {workout.index}\n")

workout_col_lst = workout.columns.tolist()
print(f"col_lst = {workout_col_lst}\n")

workout_ind_lst =workout.index.tolist()
print(f"ind_lst = {workout_ind_lst}\n")

# 单独改变某一列的列名
workout = workout.rename(columns={'re-calories':'Cal'})
print(f"column after rename re-calories to Cal: {workout.columns}\n")

# 转换回字典
workout_dict_2 = workout.to_dict()
print(f"old workout dict : \n{workout_dict}\n")
print(f"new workout dict : \n{workout_dict_2}\n")

# 选择一列
print(f"col[Cal] of workout:\n{workout['Cal']}")

workout.fillna()