from decimal import *

FILENAME = "02-26-25.txt"

def calculate_total():
    total = Decimal(0.00)
    with open(FILENAME, "r") as file:
        data = file.readlines()
        for line in data:
            print(f"Adding {line}")
            total += Decimal(line)
    return total

total_amt = calculate_total()
print(f"Mog owes {total_amt/2} of the total {total_amt}")