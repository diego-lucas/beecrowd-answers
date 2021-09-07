bigger, index = 0, 0

for i in range(100):
    n = int(input())

    if n > bigger:
        bigger = n
        index = i + 1

print(bigger)
print(index)
