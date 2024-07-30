#400 = p
#100 = w
#4 = p


year = int(input("Enter year: "))
if year <=0:
    print("Invalid year.")
elif (year%4 == 0 and year%100 != 0) or year%400 == 0  :
    print(f"{year} is a leap year.")
else :
    print(f"{year} is not a leap year.")