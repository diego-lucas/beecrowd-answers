n = int(input())

for i in range(n):
    x = int(input())
    if sum([1 for j in range(1, (x//2)+1) if x % j == 0]) == 1:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")