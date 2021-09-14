n = int(input())

wins = 0
for i in range(n):
    battle = input()

    if "CD" not in battle:
        wins += 1

print(wins)