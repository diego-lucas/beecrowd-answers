from collections import deque

nv = int(input())

for i in range(nv):
    n, k = map(int, input().split())

    group = deque(range(1, n+1))

    while len(group) > 1:
        group.rotate(-k)
        group.pop()

    last_alive = group.pop()
    print(f"Case {i+1}: {last_alive}")
