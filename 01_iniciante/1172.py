vector = []
for i in range(10):
    n = int(input())

    if n <= 0:
        n = 1
    
    vector.append(n)

for i in range(len(vector)):
    print(f"X[{i}] = {vector[i]}")