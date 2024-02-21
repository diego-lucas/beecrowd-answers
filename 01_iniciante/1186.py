operacao = input()

resultado = 0
limite = 11

for i in range (12):
    for j in range(12):
        num = float(input())
        if j > limite:
            resultado += num
    limite -= 1

if operacao == "M":
    resultado /= 66

print(f"{resultado:.1f}")