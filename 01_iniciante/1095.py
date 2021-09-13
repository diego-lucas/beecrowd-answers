for i in range(0, 21, 2):
    i = i / 10
    for j in range(1, 4):
        if int(i) == i:
            print(f"I={i:.0f} J={(j+i):.0f}")
        else:
            print(f"I={i:.1f} J={(j+i):.1f}")
