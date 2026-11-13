A,B,C = map(float,input().split())
number =[A,B,C]
number.sort(reverse=True)
A , B, C =number
if (A >= B + C):
    print("NAO FORMA TRIANGULO")
else:
    if( (A * A)==(B * B) + (C *C)):
      print("TRIANGULO RETANGULO")
    elif((A*A) > (B * B) + (C *C)):
      print("TRIANGULO OBTUSANGULO")
    elif((A*A)< (B * B) + (C *C)):
      print("TRIANGULO ACUTANGULO")
    if(A == B == C):
         print("TRIANGULO EQUILATERO")
    else:
        print("TRIANGULO ISOSCELES") 
       