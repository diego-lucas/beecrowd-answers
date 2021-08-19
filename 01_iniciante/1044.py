n1, n2 = map(int, input().split())

n1, n2 = max(n1, n2), min(n1, n2)

if n1 % n2 == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
