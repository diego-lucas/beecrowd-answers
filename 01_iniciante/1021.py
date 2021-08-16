# Sum a small digit because of the binary representation
# See more here: https://betterprogramming.pub/floating-point-numbers-are-weird-in-python-heres-how-to-fix-them-51336e4ad51a
amount = float(input()) + 0.0000001

notes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

print("NOTAS:")
for value in notes:
    num_notes = int(amount // value)
    amount %= value
    print(f"{num_notes} nota(s) de R$ {value}.00")

print("MOEDAS:")
for value in coins:
    num_coins = int(amount // value)
    amount %= value
    print(f"{num_coins} moeda(s) de R$ {value:.2f}")
