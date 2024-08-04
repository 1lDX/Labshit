# 2 hours free
# 3 

hours = int(input('Enter number of hours: '))
minutes = int(input('Enter number of minutes: '))
buyAmt = int(input('Enter shopping amount: '))

cost = 0

if (hours < 0 or hours > 20) or (minutes < 0 or minutes > 59) :
    print("Invalid time.")
elif (hours < 2 ) and minutes > 0 :
    print(f"Total amount due is {cost} Baht, thank you. ")
elif 