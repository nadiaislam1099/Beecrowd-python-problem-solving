a = float(input())
a15 =a + (a * 0.15)
a12 = a+ (a*0.12)
a10 = a + (a*0.1)
a7 = a + (a*0.07)
a4 = a + (a* 0.04)
if( a >= 0 and a <=400.00):
    print("Novo salario: %.2f" % a15)
    print("Reajuste ganho: %.2f" % (a15 - a))
    print("Em percentual: 15 %")
elif(a >= 400.01 and a <= 800.00):
    print("Novo salario: %.2f" % a12)
    print("Reajuste ganho: %.2f" % (a12 - a))
    print("Em percentual: 12 %") 
elif(a >= 800.01 and a <= 1200.00):
    print("Novo salario: %.2f" % a10)
    print("Reajuste ganho: %.2f" % (a10 - a))
    print("Em percentual: 10 %") 
elif(a >= 1200.01 and a <= 2000.00):
    print("Novo salario: %.2f" % a7)
    print("Reajuste ganho: %.2f" % (a7 - a))
    print("Em percentual: 7 %") 
else:
    print("Novo salario: %.2f" % a4)
    print("Reajuste ganho: %.2f" % (a4 - a))
    print("Em percentual: 4 %") 

