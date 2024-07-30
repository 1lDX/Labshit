#1 day == 1440 mins

import math
mins = int(input("Minutes before due: "))
tem = float(input("Temperature: "))
rain = (input("Is it raining (y/n)? "))

day = mins/1440

if mins < 2880 :
    print(f">>> {day} days before due.")
    print(">>> I will do the assignment")
elif (mins >= 2880 and mins <= 7200) and tem > 40 or (tem <25 and rain =="y") :
    print(f">>> {day} days before due.")
    print(">>> I will not do the assignment.")

elif mins > 7200 :
    print(f">>> {day} days before due.")
    print(">>> I will not do the assignment.")



    



