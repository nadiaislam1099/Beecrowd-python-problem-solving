i = 0
post = 0
even = 0
neg = 0
odd = 0
while i < 5:
    num = int(input())
    if( num % 2 == 0):
        even += 1
    if(num %2 != 0):
        odd += 1
    if (num > 0):
        post += 1
    if (num < 0):
        neg += 1

    i += 1
print(even ,"valor(es) par(es)")
print(odd ,"valor(es) impar(es)")
print(post ,"valor(es) positivo(s)")
print(neg ,"valor(es) negativo(s)")
