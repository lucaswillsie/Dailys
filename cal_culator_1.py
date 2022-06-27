days = range(365)
calorie = input("Daily Cal: ")
weight = int(input("Weight: "))

for day in days:
    print(f"Day - {day + 1} ")
    dif = float(calorie) - (float(weight) * 10)
    pound = dif / 3600
    weight = float(weight) + float(pound)
    print(weight + (dif / 3600))
