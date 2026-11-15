x = int(input())
y = int(input())
if (x > y):
        x,y = y,x
i = x + 1
sum = 0
while ( i < y):
        if (i % 2 != 0):
                sum += i
        i += 1
print(sum)