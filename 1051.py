a = float(input())
a1 = (a - 2000.00) * 0.08
a2 = (1000 * 0.08) + (a- 3000)* 0.18

a3 = (1000 * 0.08)+ (1500 * 0.18)+ (a -4500.00) * 0.28
if (a >= 0.00 and a <= 2000.00):
    print("Isento")
elif(a >= 2000.01 and a <= 3000.00):
    print("R$ %.2f" % a1)
elif(a >= 3000.01 and a <= 4500.00):
    print("R$ %.2f" % a2)
else:
     print("R$ %.2f" % a3)