code_1, amount_1, value_1 = map(float, input().split())
code_2, amount_2, value_2 = map(float, input().split())

total_value = (amount_1 * value_1) + (amount_2 * value_2)

print(f"VALOR A PAGAR: R$ {total_value:.2f}")