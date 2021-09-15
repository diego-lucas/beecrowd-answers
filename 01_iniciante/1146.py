while True:
    n = int(input())
    if n == 0:
        break
    for i in range(1, n):
        print(i, end=" ")
    print(n)