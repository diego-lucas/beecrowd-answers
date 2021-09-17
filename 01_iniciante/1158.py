n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    if x % 2 == 0:
        x += 1
    result = sum([j for j in range(x, x + (y*2), 2)])
    print(result)
