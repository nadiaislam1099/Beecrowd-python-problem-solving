age = int(input())
years = age // 365
age = age % 365
months = age // 30
age = age %30
days = age
print (years,"ano(s)")
print(months, "mes(es)")
print(days, "dia(s)")