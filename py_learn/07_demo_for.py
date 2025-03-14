#
temper_list = [33.4, 33.6, 44, 34, 35, 36, 33.8, 37]

for t in temper_list:
    if t > 38:
        print("doomed!!!")
    else:
        print(str(t) + " is fine")

# keys() , values(),items()

temper_dict = {122: 36, 123: 37, 124: 39, 125: 36.7}
for id, temp in temper_dict.items():
    if temp >= 38:
        print("staff_id :" + str(id) + " is doomed...")
    else:
        print("staff_id :" + str(id) + " is fine...")

# range(*start,*end,step) , value of *end is not include ; step is optional parameter
total = 0
for i in range(1, 101):
    total += i
print("1+..+100 =" + str(total))

''' 14
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''
def longestCommonPrefix(self, strs) -> str:
    pref = strs[0]
    len_pref = len(pref)

    for s in strs[1:]:
        while pref != s[0:len_pref]:
            len_pref -= 1
            if len_pref == 0:
                return ""

        pref = pref[0:len_pref]
    return pref
