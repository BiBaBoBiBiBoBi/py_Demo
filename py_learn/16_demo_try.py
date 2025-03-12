
import traceback
try:
    height = float(input("plz input a number1:"))
    weight = float(input("plz input a number2:"))
    res = height/weight
except ValueError:
    print("input is not a reasonable number")
except ZeroDivisionError:
    print("u cant input 0 as number2")
except Exception as e:
    # print error info
    print(f"Exception : {e}")
    traceback.print_exc()
    # write it in log
    with open("error.log","a") as log:
        log.write(f"{traceback.format_exc()} + \n")
# finally block always will run
finally:
    print("program running to the end.")

