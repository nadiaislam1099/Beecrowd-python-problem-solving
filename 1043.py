A,B,C = map(float,input().split())
trap = 0.5 * (A + B)* C
tri = A + B + C
if(A + B > C and A+ C > B and B+C > A ):
    print("Perimetro =%.1f" %tri) 
else:
    print("Area =%.1f" % trap)