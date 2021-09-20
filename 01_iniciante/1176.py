
def fibonacci(n):
    fibs = [0, 1]
    if n >= 2:
        for i in range(2, n+1):
            fibs.append(fibs[-1] + fibs[-2])
    return fibs[n]

t = int(input())

for i in range(t):
    n = int(input())
    
    fib = fibonacci(n)

    print(f"Fib({n}) = {fib}")