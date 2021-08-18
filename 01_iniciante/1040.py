n1, n2, n3, n4 = map(float, input().split())

w1, w2, w3, w4 = 2, 3, 4, 1

w_avg = ( (n1 * w1) + (n2 * w2) + (n3 * w3) + (n4 * w4) ) / 10
print(f"Media: {w_avg:.1f}")

if w_avg >= 7:
    print("Aluno aprovado.")
elif w_avg >= 5:
    print("Aluno em exame.")
    n5 = float(input())
    print(f"Nota do exame: {n5:.1f}")
    w_avg = ( w_avg + n5 ) / 2
    if w_avg >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {w_avg:.1f}")
else:
    print("Aluno reprovado.")