m, n = 1, 1

while True:
    m, n = map(int, input().split())
    m, n = min(m, n), max(m, n)
    if m <= 0:
        break
    sum = 0
    for i in range(m, n + 1):
        print(i, end=" ")
        sum += i
    print(f"Sum={sum}")