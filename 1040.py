N1,N2,N3,N4 = map(float,input().split())
average = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10
print("Media: %.1f" % average)
if (average >= 7.0):
    print("Aluno aprovado.")

elif(average >= 5.0 and average <= 6.9):
    print("Aluno em exame.")
    num = float(input())
    print("Nota do exame: %.1f" % num)
    sum = (average + num) /2
    if(sum >= 5.0):
       print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % sum)
else:
    print("Aluno reprovado.")
