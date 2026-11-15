n = int(input())
i = 0
count = 0
count2 = 0
while ( i < n):
    x = int(input())
    if (x >= 10 and x <= 20):
       count += 1
    else:
        count2 += 1
    i+=1
print(count ,"in")
print(count2 ,"out")