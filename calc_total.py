from decimal import *
import os, glob

# FILENAME = "receipts/insert_filename_here.txt" # override

RECEIPTS_FOLDER = "receipts"

def find_newest_receipt():
    list_of_files = glob.glob(os.path.join(RECEIPTS_FOLDER, '*'))
    if not list_of_files:
        return None

    newest_receipt = max(list_of_files, key=os.path.getmtime)

    print(f"Calculating total for '{newest_receipt}'...\n")
    return newest_receipt

def calculate_total(file_path):
    total = Decimal(0.00)
    with open(file_path, "r") as file:
        data = file.readlines()
        for line in data:
            print(f"Adding {line}")
            total += Decimal(line)
    return total

newest_receipt_path = find_newest_receipt()
total_amt = calculate_total(newest_receipt_path)
# total_amt = calculate_total(FILENAME) #override

print(f"You owe {total_amt/2} of the total {total_amt}")