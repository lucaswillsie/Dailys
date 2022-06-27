days = range(365)
calorie = input("Daily Cal: ")
weight = input("Weight: ")
dif = float(calorie) - (float(weight) * 10)
pound = dif / 3600

for day in days:
    print(f"Day - {day + 1} ")
    try:
        weight = float(weight) + float(pound)
    except:
        pass
    print(weight + (dif / 3600))
