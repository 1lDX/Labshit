def normal(n:str):
    return int(n)+1

def float(n:str):
    if n.count(".") > 1:
        return "ERROR"
    elif n.count(".") == 1:
        print(float(n)+1)
        return True
def comma(n):
    
    return
def fcom(n):
    return

n = str(input())
result = "ERROR"

if n not in (",."):
    result = normal(n)
print (result)

