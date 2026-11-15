i = 0
postive = 0
sum = 0
while i < 6 :
    num = float(input())
    if(num > 0):
        postive += 1
        sum += num
    
    i += 1
average = sum / postive
print(postive ,"valores positivos")
print("%.1f" % average )
