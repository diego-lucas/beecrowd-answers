salary = float(input())

if salary <= 400:
    readjustment = 1.15
elif salary <= 800:
    readjustment = 1.12
elif salary <= 1200:
    readjustment = 1.1
elif salary <= 2000:
    readjustment = 1.07
else:
    readjustment = 1.04

percentage = (readjustment - 1) * 100
new_salary = salary * readjustment
diff = new_salary - salary

print(f"Novo salario: {new_salary:.2f}")
print(f"Reajuste ganho: {diff:.2f}")
print(f"Em percentual: {percentage:.0f} %")
