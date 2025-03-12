# compare symbol : == ,!= ,<= ,>= ,< ,>
a = 100
if a > 99:
    print("true")
    a -= 10
else:
    a = +100
    print("a:" + a)

b = 22

if a > 80:
    print("state 1")
    if b > 20:
        print("State 2-1")
    else:
        print("state 2-2")
elif a > 60:
    print("state 1-2")
else:
    print("state 1-3")

# logic calculator
# [Please pay attention to the order of operations for logical operators.]
# not  >  and  > or
x = 12
b1 = x > 5 and x < 100 or x > -1

