a,b,c,d = map(int,input().split())
start = a * 60 + b
end = c * 60 + d
duration = end - start
if ( duration <= 0):
    duration += 24 * 60


hour = duration // 60
min = duration % 60
print("O JOGO DUROU" ,hour, "HORA(S) E",min, "MINUTO(S)")