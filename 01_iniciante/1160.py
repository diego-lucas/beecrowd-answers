t = int(input())

for i in range(t):
    pa, pb, g1, g2 = map(float, input().split())
    g1, g2 = g1 / 100, g2 / 100
    years = 0
    while pa <= pb:
        years += 1
        pa += int(pa * g1)
        pb += int(pb * g2)
        if years > 100:
            print("Mais de 1 seculo.")
            break
    if years <= 100:
        print(f"{years} anos.")