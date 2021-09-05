n1 = int(input())
n2 = int(input())

n1, n2 = min(n1, n2), max(n1, n2)

odd_sum = 0

for i in range(n1 + 1, n2):
    if i % 2 != 0:
        odd_sum += i

print(odd_sum)