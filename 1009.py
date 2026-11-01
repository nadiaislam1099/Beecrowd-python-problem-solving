name = input()
salary = float(input())
sold = float(input())

comission = sold * 0.15
total = salary + comission
print("TOTAL = R$ %.2f" % total)