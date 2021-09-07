n = int(input())

for i in range(n):
    value = int(input())

    desc = ""

    if value == 0:
        desc = "NULL"
    else:
        if value % 2 == 0:
            desc += "EVEN "
        else:
            desc += "ODD "
        if value > 0:
            desc += "POSITIVE"
        elif value < 0:
            desc += "NEGATIVE"

    print(desc)