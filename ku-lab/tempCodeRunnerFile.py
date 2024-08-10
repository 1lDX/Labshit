n = int(input())
count = 1
while True:
    z = int(input())
    if n == 0:
        count = count-1
        break    
    if z > n :
        count = count+1
        n += z-n
    if z == -1:
        break
print(count)