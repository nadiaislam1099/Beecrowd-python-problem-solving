print("MUITO OBRIGADO")
alcohol = 0
gasolina = 0
diesel = 0
while True:
    num = int(input())
    if (num < 1 and num > 4):
        continue
    elif (num == 1):
        alcohol += 1
    elif(num == 2):
        gasolina += 1
    elif(num == 3):
        diesel += 1
    elif(num == 4):
        break

print("Alcool:", alcohol)
print("Gasolina:", gasolina) 
print("Diesel:", diesel)