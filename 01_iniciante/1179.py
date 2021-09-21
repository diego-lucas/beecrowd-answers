even, odd = [], []

for i in range(15):
    n = int(input())

    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

    if len(even) == 5:
        for j in range(5):
            print(f"par[{j}] = {even[j]}")
        even = []
    elif len(odd) == 5:
        for j in range(5):
            print(f"impar[{j}] = {odd[j]}")
        odd = []

for j in range(len(odd)):
    print(f"impar[{j}] = {odd[j]}")
for j in range(len(even)):
    print(f"par[{j}] = {even[j]}")