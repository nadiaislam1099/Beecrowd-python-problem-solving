count = 0
inter = 0
gremio = 0
empates = 0
while True:
    a,b = map(int,input().split())
    count += 1
    if(a >b):
        inter += 1
    elif(b > a):
        gremio += 1
    elif(a == b):
        empates += 1


    print("Novo grenal (1-sim 2-nao)")
    num = int(input())
    if(num == 1):
        continue
    elif(num == 2):
        break

print(count,"grenais")
print("Inter:",inter,sep="")
print("Gremio:",gremio,sep="")
print("Empates:",empates,sep="")
if (inter > gremio):
    print("Inter venceu mais")
elif(gremio > inter):
    print("Gremio venceu mais")

