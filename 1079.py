n = int(input())
i = 0
num= [0]  * n
while i < n:
    a,b,c= map(float,input().split())
    num [i]= ((a * 2) + (b * 3) + (c * 5) ) /  10
    i += 1
i = 0
while i < n:
    print ("%.1f" % num[i])
    i += 1