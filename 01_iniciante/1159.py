while True:
    
    x = int(input())

    if x == 0:
        break

    if x % 2 != 0:
        x += 1

    result = sum([i for i in range(x, x+10, 2)])
    print(result)
