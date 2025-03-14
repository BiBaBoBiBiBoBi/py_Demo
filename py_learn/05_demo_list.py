# list is variable,bool/str/int/float is un-variable
shopping_list = ["keyboard", "screen", "mouse"]
print(shopping_list)
# add
shopping_list.append("headphone")
print(shopping_list)
# delete
shopping_list.remove("screen")
print(shopping_list)

# and u can put different type of variables in the same list
shopping_list.append(132)
shopping_list.append(True)
print(shopping_list)
lengthOfList = len(shopping_list)
print(shopping_list[2])

shopping_list[2] = "changed Elements"
print(shopping_list[2])

# max min sorted
int_list = [12, 23, 44, 1, 4, 11, -99]
print(int_list)
print("sorted list \n:" + str(sorted(int_list)))
print(max(int_list))
print(min(int_list))
ls = sorted(int_list, key=lambda i: len(str(i)), reverse=False)

# slice operation  sequence[start:stop:step]
reverse_list = int_list[::-1]

print(reverse_list)
lst = [1, 2, 3, 4, 5]
sub_lst = lst[1:4]  # 从索引1到索引4（不包含4）
print(sub_lst)  # 输出：[2, 3, 4]
# reverse string
s = "hello"
reversed_s = s[::-1]
print(reversed_s)  # 输出：'olleh'

pop_a = lst.pop() # remove last element of list and return it
print(pop_a)
print(lst)
