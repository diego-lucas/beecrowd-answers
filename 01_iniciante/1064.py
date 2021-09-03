positive_values = 0
mean = 0

for i in range(6):
    value = float(input())

    if value > 0:
        mean += value
        positive_values += 1

mean /= positive_values
print(f"{positive_values} valores positivos")
print(f"{mean:.1f}")
