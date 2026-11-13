a,b = map(int,input().split())
duration = b - a
duration2 = (24 - a) + b
if(a == b):
    print("O JOGO DUROU 24 HORA(S)")
elif(a <  b):
    print("O JOGO DUROU" ,duration, "HORA(S)")
elif(a > b):
    print("O JOGO DUROU" ,duration2, "HORA(S)")
