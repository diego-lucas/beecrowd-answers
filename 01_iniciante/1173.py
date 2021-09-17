n = int(input())

vector = [n]
for i in range(9):
    vector.append(vector[-1]*2)

for i, x in enumerate(vector):
    print(f"N[{i}] = {x}")