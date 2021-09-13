grades = []
while len(grades) < 2:
    n = float(input())

    if 0 <= n <= 10:
        grades.append(n)
    else:
        print("nota invalida")

mean = sum(grades) / 2
print(f"media = {mean:.2f}")