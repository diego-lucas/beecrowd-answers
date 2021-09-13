n = int(input())

for i in range(n):

    n1, n2 = map(int, input().split())

    try:
        result = n1 / n2
        print(f"{result:.1f}")
    except:
        print("divisao impossivel")
