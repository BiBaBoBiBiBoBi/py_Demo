#
temper_list=[33.4,33.6,44,34,35,36,33.8,37]

for t in temper_list:
    if t>38:
        print("doomed!!!")
    else:
        print(str(t)+" is fine")

# keys() , values(),items()

temper_dict= {122:36,123:37,124:39,125:36.7}
for id,temp in temper_dict.items():
    if temp>=38:
        print("staff_id :"+str(id)+ " is doomed...")
    else:
        print("staff_id :"+str(id)+ " is fine...")

# range(*start,*end,step) , value of *end is not include ; step is optional parameter
total = 0
for i in range(1,101):
    total += i
print("1+..+100 ="+str(total))