from decimal import *

# TODO: make filename dynamic

FILENAME = "05-12-25.txt"

def calculate_total():
    total = Decimal(0.00)
    with open(FILENAME, "r") as file:
        data = file.readlines()
        for line in data:
            print(f"Adding {line}")
            total += Decimal(line)
    return total

total_amt = calculate_total()
print(f"You owe {total_amt/2} of the total {total_amt}")