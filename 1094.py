num = int(input())
C= 0 
R = 0 
S =0 
i = 0

while i < num:
    count, animal = input().split()
    count = int(count)
    if ( animal == "C"):
        C += count
    elif(animal == "R"):
        R += count
    elif(animal == "S"):
        S += count 
    i += 1

total = C + R + S
cper = (C / total) * 100
rper = (R / total) * 100
sper = (S / total) * 100
print ("Total:", total ,"cobaias")
print("Total de coelhos:" , C)
print("Total de ratos:" , R)
print("Total de sapos:" , S)
print("Percentual de coelhos: %.2f"  % cper,"%")
print("Percentual de ratos: %.2f"  % rper,"%")
print("Percentual de sapos: %.2f"  % sper,"%")