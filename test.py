money = int(input())

    
if money >= 1000:
    k = money // 1000
    money = money - 1000*k
if money >= 500:
    fiveh = money // 500
    money = money - 500*fiveh
if money >= 100:
    h = money // 100
    money = money - 100*h
if money >= 50:
    fifty = money // 50
    money = money - 50*fifty
if money >= 20:
    twenty = money //20
    money = money - 20*twenty

if money >= 10:
    coin10 = money //10
    money = money - 10*coin10
if money >= 5:
    coin5 = money //5
    money = money - 5*coin5
if money >= 2:
    coin2 = money //2
    money = money - 2*coin2
if money >= 1:
    coin1 = money //1
    money = money - 1*coin1
    
print(f"1000 : {k}")
print(f"500 : {fiveh}")
print(f"100 : {h}")
print(f"50 : {fifty}")
print(f"20 : {twenty}")
print(f"10 : {coin10}")
print(f"5 : {coin5}")
print(f"2 : {coin2}")
print(f"1 : {coin1}")






    