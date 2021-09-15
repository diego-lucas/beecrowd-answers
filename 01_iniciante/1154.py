ages = []

while True:

    age = int(input())
    if age < 0:
        break
    ages.append(age)

mean_age = sum(ages) / len(ages)
print(f"{mean_age:.2f}")
