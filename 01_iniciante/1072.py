n = int(input())

in_values = 0

for i in range(n):
    value = int(input())

    if 10 <= value <= 20:
        in_values += 1

out_values = n - in_values

print(f"{in_values} in")
print(f"{out_values} out")
