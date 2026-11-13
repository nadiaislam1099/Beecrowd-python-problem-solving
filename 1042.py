a,b,c = map(int,input().split())
if(a <= b and a <= c):
    if(b<c):
      print(a)
      print(b)
      print(c)
    else:
       print(a)
       print(c)
       print(b)
elif(b <= a and b<=c ):
   if(a<c):
      print(b)
      print(a)
      print(c)
   else:
      print(b)
      print(c)
      print(a)
elif(c<=a and c<=b):
   if(a<b):
      print(c)
      print(a)
      print(b)
   else:
      print(c)
      print(b)
      print(a)

else:
   print()

print()

print(a)
print(b)
print(c)