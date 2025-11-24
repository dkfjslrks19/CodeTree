ages = []

while True:
    age = int(input())
    if age >= 30:
        break
    ages.append(age)

print(f"{sum(ages)/len(ages):.2f}")