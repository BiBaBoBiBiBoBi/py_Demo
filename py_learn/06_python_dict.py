# list -> []
# dict -> {} key must be value(un-changeable)

contacts = {"john":132 ,"lily":142}
# add
contacts["sam"]=166
#update
contacts["john"]= 199
print(contacts)
contacts.pop("lily")
print(contacts)

# tuple->() un-changeable
guy = ("john",23)
name = guy[0]
age= guy[1]
contacts[guy]=46

print(contacts)

# truncate all the elements
contacts.clear()

# exist
b_check = "john" in contacts
# delete
if b_check:
    del contacts["john"]
    print("delete success! ")
    print(contacts)
else:
    print("key : "+ str("john") +" not exists in dic[contacts]")