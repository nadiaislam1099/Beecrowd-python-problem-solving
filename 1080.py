highest = int(input())
i = 2
position = 1
while i <= 100:
    num = int(input())
    if ( num > highest):
        highest = num
        position = i
    i += 1
print(highest)
print(position)