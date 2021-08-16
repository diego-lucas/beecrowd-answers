cod, amount = map(int, input().split())

prices = {
    1: 4,
    2: 4.5,
    3: 5,
    4: 2,
    5: 1.5,
}

total = amount * prices[cod]

print(f"Total: R$ {total:.2f}")
