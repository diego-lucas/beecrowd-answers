n = int(input())

animals = {
    "C": 0,
    "R": 0,
    "S": 0
}

for i in range(n):
    amount, type = input().split()
    amount = int(amount)

    animals[type] += amount

total = sum(animals.values())
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {animals['C']}")
print(f"Total de ratos: {animals['R']}")
print(f"Total de sapos: {animals['S']}")
print(f"Percentual de coelhos: {(animals['C']/total)*100:.2f} %")
print(f"Percentual de ratos: {(animals['R']/total)*100:.2f} %")
print(f"Percentual de sapos: {(animals['S']/total)*100:.2f} %")
