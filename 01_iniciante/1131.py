exit = 1

inter_wins = 0
gremio_wins = 0
ties = 0

while exit == 1:
    
    inter_score, gremio_score = map(int, input().split())

    if inter_score > gremio_score:
        inter_wins += 1
    elif inter_score < gremio_score:
        gremio_wins += 1
    else:
        ties += 1

    print("Novo grenal (1-sim 2-nao)")
    exit = int(input())

total = inter_wins + gremio_wins + ties
print(f"{total} grenais")
print(f"Inter:{inter_wins}")
print(f"Gremio:{gremio_wins}")
print(f"Empates:{ties}")

if inter_wins > gremio_wins:
    print("Inter venceu mais")
elif inter_wins < gremio_wins:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
