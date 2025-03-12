# input func
# age=input("type ur age below..\n")
# print("Now I know ur age is :"+age)
#
# print("And u should know that all variables come from input() func is Type "+str(type(age)))

# str -> int
res_01 = 33 + int("233")
print(res_01)
# str/int -> float
res_03 = float("2.32342")
res_03 = float(1233)
# other -> str
res_02 = str(type(True))

# practice BMI calculator
weight = input("plz input ur weight(kg):")
height = input("plz inpur ur height(m):")
user_BMI = float(weight) / (float(height) ** 2)
print("Here is ur body BMI:" + str(user_BMI))
