day1= int(input().split()[1])
hr,min,sec= map(int,input().split(":"))
day2= int(input().split()[1])
hr1,min1,sec1= map(int,input().split(":"))
start = day1 * 86400 + hr * 3600 + min * 60 + sec
end = day2 * 86400 + hr1 * 3600 + min1 * 60 + sec1
duration = end - start

day = duration // 86400
duration = duration % 86400

hour = duration // 3600
duration= duration % 3600

minute = duration // 60
secon = duration % 60
print (day ,"dia(s)")
print (hour ,"hora(s)")
print (minute ,"minuto(s)")
print (secon ,"segundo(s)")