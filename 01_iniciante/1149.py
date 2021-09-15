# Filter only the positive numbers in the input list
a, n = filter(lambda x: x > 0, map(int, input().split()))

sum = sum([a + i for i in range(n)])
print(sum)
