# 2 hours free
# 3 and 4 hours per 20
# 5 hours per 50
# minute++
# if pay 300-3000 free 3-4 hours
# if pay 3001 free
hours = int(input('Enter number of hours: '))
minutes = int(input('Enter number of minutes: '))
buyAmt = int(input('Enter shopping amount: '))
if (minutes < 0 or minutes > 59) or (hours > 20) or (minutes > 1200):
    print("Invalid time.")
else: 
    if minutes > 0:
        hours = hours+1
        allmins = (hours*60)
        range_mins = 0
        cost = 0
        free = 120
        if buyAmt>= 300 and buyAmt<=3000:
            free = 240
        while range_mins<=allmins:
            if buyAmt > 3001:
                break
            if range_mins > free:
                if range_mins/60 >=5 :
                    cost = cost +50
                else : cost = cost+20
            range_mins += 60
        if buyAmt > 3001:
            print("No charge, thank you.")
        else :
            print(f'total amount due is {cost} Baht, thank you.')