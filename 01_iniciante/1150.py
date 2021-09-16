x = int(input())
z = int(input())

while z <= x:
    z = int(input())

sum = 0
counter = 0
while sum < z:
    sum += x
    x += 1
    counter += 1
print(counter)