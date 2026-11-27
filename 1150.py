a = int(input())
b = int(input())
while b <= a:
    b = int(input())
count = 0
sum = 0
for i in range (a ,b +1):
    sum += i
    count += 1
    if sum > b:
        break

print(count)