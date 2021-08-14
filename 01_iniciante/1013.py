a, b, c = map(int, input().split())

bigger_a_b = (a + b + abs(a - b)) / 2
bigger = (bigger_a_b + c + abs(bigger_a_b - c)) / 2

print(f"{bigger:.0f} eh o maior")