amount= float(input())
value = round(amount * 100)
print("NOTAS:")
note100 = value // 10000
value = value % 10000
note50 = value // 5000
value = value % 5000

note20 = value // 2000
value = value % 2000

note10= value // 1000
value = value % 1000

note5 = value // 500
value = value % 500

note2 = value // 200
value = value % 200
print(note100 ,"nota(s) de R$ 100.00")
print(note50 ,"nota(s) de R$ 50.00")
print(note20,"nota(s) de R$ 20.00")
print(note10 ,"nota(s) de R$ 10.00")
print(note5 ,"nota(s) de R$ 5.00")
print(note2 ,"nota(s) de R$ 2.00")

print("MOEDAS:")
note1 = value // 100
value = value % 100
note050 = value // 50
value = value % 50
note025 = value // 25
value = value % 25
note010 = value // 10
value = value % 10
note005 = value // 5
value = value % 5
note001 = value // 1
value = value % 1
print(note1 ,"moeda(s) de R$ 1.00")
print(note050 ,"moeda(s) de R$ 0.50")
print(note025 ,"moeda(s) de R$ 0.25")
print(note010 ,"moeda(s) de R$ 0.10")
print(note005 ,"moeda(s) de R$ 0.05")
print(note001 ,"moeda(s) de R$ 0.01")