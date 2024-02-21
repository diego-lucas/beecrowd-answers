operacao = input()

resultado = 0
limite = 11

for linha in range (12):
    for coluna in range(12):
        num = float(input())
        if coluna < linha and coluna > limite:
            resultado += num
    limite -= 1

if operacao == "M":
    resultado /= 30

print(f"{resultado:.1f}")