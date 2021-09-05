even_values = 0

for i in range(5):
    value = int(input())

    if value % 2 == 0:
        even_values += 1

print(f"{even_values} valores pares")
