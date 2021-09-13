x, y = 1, 0

while x != y:
    x , y = map(int, input().split())

    if x < y:
        print("Crescente")
    elif y < x:
        print("Decrescente")