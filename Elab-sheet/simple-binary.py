n = int(input("Enter Binary digits: "))
result = 0
i = 0
summ = 0
while True:
   result = n%10
   summ += result*(2**i)
   n = n//10
   i = i+1
   if n == 0 :
      break
print(summ)