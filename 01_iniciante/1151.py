n = int(input())

fibs = [0, 1]
if n > 2:
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
fibs_str = list(map(str, fibs))
print(" ".join(fibs_str[:n]))