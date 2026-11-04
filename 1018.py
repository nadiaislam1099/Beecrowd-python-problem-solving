amount= int(input())
print(amount)
notes100 = amount // 100
amount = amount % 100
notes50 = amount // 50
amount = amount % 50
notes20 = amount // 20
amount = amount % 20
notes10= amount // 10
amount = amount % 10
notes5 = amount // 5
amount = amount % 5
notes2 = amount // 2
amount = amount % 2
notes1 = amount // 1
amount = amount % 1

print(notes100 ,"nota(s) de R$ 100,00")
print(notes50 ,"nota(s) de R$ 50,00")
print(notes20 ,"nota(s) de R$ 20,00")
print(notes10 ,"nota(s) de R$ 10,00")
print(notes5 ,"nota(s) de R$ 5,00")
print(notes2 ,"nota(s) de R$ 2,00")
print(notes1 ,"nota(s) de R$ 1,00")

