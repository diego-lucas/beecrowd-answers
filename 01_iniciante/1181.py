L = int(input())
T = input()
matrix = []

for i in range(12):
    row = []
    for j in range(12):
        n = float(input())
        row.append(n)
    matrix.append(row)

if T == "S":
    result = sum(matrix[L])
else:
    result = sum(matrix[L]) / 12

print(f"{result:.1f}")
