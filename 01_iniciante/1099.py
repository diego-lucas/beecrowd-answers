n = int(input())

for i in range(n):
    
    x, y = map(int, input().split())
    x, y = min(x, y), max(x, y)

    sum = 0
    for j in range(x+1, y):
        if j % 2 != 0:
            sum += j
    print(sum)
