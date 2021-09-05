even_values, odd_values, positive_values, negative_values = 0, 0, 0, 0

for i in range(5):
    value = int(input())

    if value % 2 == 0:
        even_values += 1
    else:
        odd_values += 1
    if value > 0:
        positive_values += 1
    elif value < 0:
        negative_values += 1

print(f"{even_values} valor(es) par(es)")
print(f"{odd_values} valor(es) impar(es)")
print(f"{positive_values} valor(es) positivo(s)")
print(f"{negative_values} valor(es) negativo(s)")
