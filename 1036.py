import math
A,B,C = map(float,input().split())
D=(B*B - 4 *A*C)
if( A == 0 or D < 0):
    print("Impossivel calcular")
else:
   R1 = (-B+ math.sqrt(D)) / (2*A)
   R2 = (-B- math.sqrt(D))/ (2*A)
   print("R1 = %.5f" %R1)
   print("R2 = %.5f" %R2)
## Maintain the line ,space and sequence otherwise runtime error will come(After else)