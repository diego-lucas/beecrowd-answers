# Native function to find maximum common divisor
from math import gcd

n = int(input())

for i in range(n):
    f1, f2 = map(int, input().split())
    mdc = gcd(f1, f2)
    print(mdc)