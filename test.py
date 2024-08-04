number = 100  # ตัวเลขที่ต้องการหาร
divisor = 2   # ตัวหาร
count = 0     # ตัวแปรนับจำนวนครั้ง

while number % divisor == 0:
    number = number // divisor
    count += 1

print("จำนวนครั้งที่หารได้:", count)