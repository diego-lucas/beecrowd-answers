salary = float(input())

final_tax = 0
if salary >= 4500:
    amount = salary - 4500
    final_tax += amount * 0.28
    salary -= amount
if salary >= 3000:
    amount = salary - 3000
    final_tax += amount * 0.18
    salary -= amount
if salary >= 2000:
    amount = salary - 2000
    final_tax += amount * 0.08
    salary -= amount

if final_tax == 0:
    print("Isento")
else:
    print(f"R$ {final_tax:.2f}")
