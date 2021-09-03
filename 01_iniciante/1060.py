positive_values = 0

for i in range(6):
    value = float(input())

    if value > 0:
        positive_values += 1

print(f"{positive_values} valores positivos")
