while True:
  a,b = map(int,input().split())

  if ( a<= 0 or b <= 0):
    break
  
  if a > b:
    a,b= b,a

  total = 0
  for i in range (a,b+1):
    total += i
    print(i, end=" ")

  print("Sum=", total ,sep ="")