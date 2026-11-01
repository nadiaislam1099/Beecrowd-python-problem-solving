A,B,C = input().split()

ques1 =0.5 * float(A) * float(C)
ques2 = 3.14159 * float(C) ** 2
ques3 = 0.5 * (float(A) +  float(B) ) * float(C)
ques4 = float(B) ** 2
ques5 = float(A) * float(B)

print("TRIANGULO: %.3f" %ques1)
print("CIRCULO: %.3f"% ques2)
print("TRAPEZIO: %.3f" %ques3)
print("QUADRADO: %.3f"% ques4)
print("RETANGULO: %.3f"%ques5)