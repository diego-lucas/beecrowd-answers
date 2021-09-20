vector = [float(input()) for i in range(100)]

for i in range(len(vector)):
    if vector[i] <= 10:
        print(f"A[{i}] = {vector[i]}")
