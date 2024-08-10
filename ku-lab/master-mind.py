#1234
#5341
#No positions correct, three digits correct

target = int(input("Enter a target (4-digit integer): "))
n = int(input("Enter your guess (4-digit integer): "))
i = 0
x = n
z = target
target_check = 0
n_check = 0

count = 0
while i<4:
    target_check = z % 10
    while i<4:
        n_check = x % 10
        if target_check == n_check:
            count = count+1
        x = x//10
    z = z//10
    
    