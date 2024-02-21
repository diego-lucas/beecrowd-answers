operacao = input()

resultado = 0

for i in range (12):
    for j in range(12):
        num = float(input())
        if j < i:
            resultado += num

if operacao == "M":
    resultado /= 66

print(f"{resultado:.1f}")