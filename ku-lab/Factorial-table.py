# 0! = 1 = 1
# 1! = 1 = 1
# 2! = 2 x 1 = 2
# 3! = 3 x 2 x 1 = 6
# 4! = 4 x 3 x 2 x 1 = 24
# 5! = 5 x 4 x 3 x 2 x 1 = 120



n = int(input())
i = 0
c = 0
if n < 0:
    print ("Invalid input, program terminates.")
else :
    while i<=n :  
        print(f"{i}! = ", end="")
        print(f"{i} x "*i)

        c+=1
        i+=1
    while i<=n :
        break