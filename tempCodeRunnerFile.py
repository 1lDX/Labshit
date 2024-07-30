import math
minutes = int(input("Minutes before due: "))
temperature = float(input("Temperature: "))
raining = input("Is it raining (y/n)? ").upper

total = round(minutes/1440)
if total == 0 :
    total = 1
print(f">>> {total} days before due.")
if total > 5:
    print(">>> I will not do the assignment") 
elif total < 2  :
    print(">>> I will do the assignment.")
    if temperature > 40 or (temperature > 25 and raining == 'Y'):
        print(">>> I will do the assignment.")
    else:
        print(">>> I will do the assignment.")
    
