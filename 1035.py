A,B,C,D = map(int,input().split())
sum1 = C + D
sum2 = A + B 
if( B > C and D > A):
    if(sum1 > sum2):
        if(C >=0 and D >= 0):
            if (A % 2 == 0):
                print("Valores aceitos")
            else:
               print("Valores nao aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")  
else:
    print("Valores nao aceitos")