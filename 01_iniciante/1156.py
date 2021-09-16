s = 0
q = 1

for i in range(1, 40, 2):
    s += i / q
    q *= 2

print(f"{s:.2f}")
