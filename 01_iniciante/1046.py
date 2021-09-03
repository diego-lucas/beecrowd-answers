begin, end = map(int, input().split())

if end <= begin:
    end += 24

duration = end - begin

print(f"O JOGO DUROU {duration} HORA(S)")
