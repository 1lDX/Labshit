time = int(input())
    
hrs = time//60
minute = time%60
days = hrs//24

if hrs < 1 and minute <2:
    print(f"{minute} minute")
elif hrs < 1 and minute >1:
    print(f"{minute} minutes")
elif hrs == 1 and hrs < 24 and minute == 0:
    print(f"{hrs} hour")
elif hrs > 1 and hrs < 24 and minute == 0:
    print(f"{hrs} hours")    

    
elif hrs > 1 and hrs < 24 and minute == 0:
    print(f"{hrs} hours")
elif hrs > 1 and hrs < 24 and minute == 1:
    print(f"{hrs} hours {minute} minute")
elif hrs > 1 and hrs < 24 and minute > 1:
    print(f"{hrs} hours {minute} minutes")    
    
    
elif hrs > 1 and hrs < 24 and minute == 0:
    print(f"{hrs} hours {minute} minute")
elif hrs > 1 and hrs < 24 and minute > 1:
    print(f"{hrs} hours {minute} minutes")
    

elif days == 1 and minute == 0:
    print(f"{days} day")
elif days == 1 and minute == 1:
    print(f"{days} day {minute} minute")
elif days == 1 and minute >= 1:
    print(f"{days} day {minute} minutes")

elif days > 1 and minute == 0:
    print(f"{days:.0f} days")
elif days > 1 and minute > 1:
    print(f"{days:.0f} days {minute} minutes")
    

    