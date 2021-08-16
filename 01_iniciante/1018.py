amount = int(input())

values = [100, 50, 20, 10, 5, 2, 1]

print(amount)
for value in values:
    notes = amount // value
    amount %= value
    print(f"{notes} nota(s) de R$ {value},00")
