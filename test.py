c = 0
last_height = 0
while True:
    height = int(input())
    if height == -1:
        break
    if height > last_height:
        c += 1
        last_height = height

print(c)