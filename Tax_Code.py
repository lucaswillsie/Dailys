Rev = input("""
Yearly - Pay each year - 1
Monthly - Pay each month - 2
Weekly - Pay each week - 3
""").lower()
pay = input(int(f"How much do you get paid {Rev}: "))

def Tax_bracket(TAX):
    if pay < 9950:
        TAX = TAX * .10
        return
    elif 9951 <= pay <= 40525:
        TAX = TAX * .12
        return
    elif 40526 <= pay <= 86375:
        TAX = TAX * .22
        return
    elif 86376 <= pay <= 164925:
        TAX = TAX * .24
        return
    elif 164926 <= pay <= 209425:
        TAX = TAX * .32
        return
    elif 209426 <= pay <= 523600:
        TAX = TAX * .35
        return
    elif 523601 <= pay:
        TAX = TAX *.37
        return
        

if Rev == "1" or "yearly":
    print(f"this year you owe {Tax_bracket()}")
elif Rev == "2" or "monthly":
    print(f"this year you owe {Tax_bracket() * 12}")
elif Rev == "3" or "weekly":
    print(f"this year you owe {Tax_bracket() * 52}")Rev = input("""
Yearly - Pay each year - 1
Monthly - Pay each month - 2
Weekly - Pay each week - 3
""").lower()
pay = input(int(f"How much do you get paid {Rev}: "))

def Tax_bracket(TAX):
    if pay < 9950:
        TAX = TAX * .10
        return
    elif 9951 <= pay <= 40525:
        TAX = TAX * .12
        return
    elif 40526 <= pay <= 86375:
        TAX = TAX * .22
        return
    elif 86376 <= pay <= 164925:
        TAX = TAX * .24
        return
    elif 164926 <= pay <= 209425:
        TAX = TAX * .32
        return
    elif 209426 <= pay <= 523600:
        TAX = TAX * .35
        return
    elif 523601 <= pay:
        TAX = TAX *.37
        return
        

if Rev == "1" or "yearly":
    print(f"this year you owe {Tax_bracket()}")
elif Rev == "2" or "monthly":
    print(f"this year you owe {Tax_bracket() * 12}")
elif Rev == "3" or "weekly":
    print(f"this year you owe {Tax_bracket() * 52}")
