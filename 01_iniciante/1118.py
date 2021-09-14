grades = []
while True:
    n = float(input())

    if 0 <= n <= 10:
        grades.append(n)
    else:
        print("nota invalida")

    if len(grades) == 2:
        mean = sum(grades) / 2
        print(f"media = {mean:.2f}")

        while True:
            print("novo calculo (1-sim 2-nao)")
            new_mean = int(input())
            if new_mean == 2:
                exit()
            elif new_mean == 1:
                grades = []
                break
