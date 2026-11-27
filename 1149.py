data = list(map(int, input().split()))

A = data[0]
N = data[1]
index = 2

while N <= 0:
    N = data[index]
    index += 1

total = 0

for i in range(A, A + N):
    total += i

print(total)

