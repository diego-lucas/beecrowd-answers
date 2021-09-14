x, y = map(int, input().split())

i = 0
counter = 0
while i < y:
    counter += 1
    i += 1
    if counter == x:
        print(i)
        counter = 0
    else:
        print(i, end=" ")
