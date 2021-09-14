from collections import defaultdict

option = 0

result = defaultdict(int)

while option != 4:
    option = int(input())
    if option in [1, 2, 3]:
        result[option] += 1

print("MUITO OBRIGADO")
print(f"Alcool: {result[1]}")
print(f"Gasolina: {result[2]}")
print(f"Diesel: {result[3]}")