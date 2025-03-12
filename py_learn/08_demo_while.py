#
from itertools import count
from time import sleep

def measure_brightness():
    print("I am func() measure_brightness.")

def while_test():
    i = 0
    while i < 10:
        i += 1
        # sleep(1)
        # print("start sleep "+str(i)+" sec")

    # print("sleep end")

    user_input = input("input some numbers to calc avg,type 'q' to end input:")
    sum = 0
    cnt = 0
    while user_input != 'q':
        user_input = input("input some numbers to calc avg,type 'q' to end input:")
        if user_input != 'q':
            cnt += 1
            sum += float(user_input)

    if count == 0:
        avg = 0
    else:
        avg = sum / cnt
    print(avg)

# 跳转语句
# break return continue
def jump_sentence():
    for i in range(1, 20):
        if i< 15:
            continue
        elif i<18:
            print("i > 15",i)
        else:
            print("ready to break",i)
            break


if __name__ == '__main__':
    jump_sentence()
    # while_test()