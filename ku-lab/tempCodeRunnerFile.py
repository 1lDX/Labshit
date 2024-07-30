#1 day == 1440 mins

import math
min = int(input("Minutes before due: "))
t = int(input("Temperature: "))
rain = (input("Is it raining (y/n)? "))

day = min/1440

if min > 2880 :
 print(f">>> {day:.0f} days before due.")
 print(">>> I will do the assignment")
