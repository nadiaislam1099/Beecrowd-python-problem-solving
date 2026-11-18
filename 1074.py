n = int(input())
x = [0]  * n
i = 0


  
while i < n:
    x[i]= int(input())
    i += 1

i = 0
while i < n:
    num = x[i]
    if(num % 2 == 0 and num > 0):
     print("EVEN POSITIVE")
    elif(num % 2 == 0 and num < 0):
     print("EVEN NEGATIVE")
    elif(num % 2 != 0 and num > 0):
     print("ODD POSITIVE")
    elif(num % 2 != 0 and num < 0):
     print("ODD NEGATIVE")
    else :
     print("NULL")
    
    i += 1

