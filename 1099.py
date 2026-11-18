n = int(input())

numbers = [0] * n

i = 0
while i < n:
    x, y = map(int, input().split())
    numbers[i] = (x, y)
    i += 1

i = 0
while i < n:
    x, y = numbers[i]

    if x > y:
        x, y = y, x

    total = 0
    j = x + 1

    while j < y:
        if j % 2 != 0:
            total += j
        j += 1

    print(total)
    i += 1