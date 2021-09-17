n = int(input())

for i in range(n):
    x = int(input())

    is_perfect = x == sum([j for j in range(1, (x//2)+1) if x % j == 0])

    if is_perfect:
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")