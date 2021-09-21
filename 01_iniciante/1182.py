L = int(input())
T = input()

sum = 0
for i in range(12):
    for j in range(12):
        n = float(input())
        if j == L:
            sum += n

if T == "S":
    result = sum
else:
    result = sum / 12

print(f"{result:.1f}")
