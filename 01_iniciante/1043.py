a, b, c = map(float, input().split())

if (
    (a + b > c) and
    (a + c > b) and
    (b + c > a)
    ):
    perimeter = a + b + c
    print(f"Perimetro = {perimeter:.1f}")
else:
    area = ((a + b) * c ) /  2
    print(f"Area = {area:.1f}")
