n = int(input())

if n % 2 == 0:
    n += 1

for i in range(n, n+12, 2):
    print(i)
