while True:
    a = float(input())
    if (a < 0 or a > 10):
        print("nota invalida")
    else:
        break

 
while True:
    b = float(input())
    if (b < 0 or b> 10):
        print("nota invalida")
    else:
        break

result = (a + b )/ 2
print("media = %.2f" % result)  
