n = int(input())

for i in range(1, (n*4)+1, 4):
    n1, n2, n3 = i, i+1, i+2
    print(f"{n1} {n2} {n3} PUM")