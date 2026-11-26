while True:
    a = float(input())
    if (a < 0 or a > 10.0):
        print("nota invalida")
    else:
        break

 
while True:
    b = float(input())
    if (b < 0 or b> 10.0):
        print("nota invalida")
    else:
        break

result = (a + b )/ 2
print("media = %.2f" % result) 

while True:
    print("novo calculo (1-sim 2-nao)")
    num = int(input())
    if(num < 1 or num > 2):
       continue

    elif(num == 1):
       while True:
        p = float(input())
        if (p < 0 or p > 10.0):
          print("nota invalida")
        else:
          break 
       while True:
         q = float(input())
         if (q < 0 or q > 10.0):
          print("nota invalida")
         else:
          break
       result1 = (p + q )/ 2
       print("media = %.2f" % result1)  
    elif(num == 2):
      break
     
     