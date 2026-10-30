#IMPORT
import time

#VARIABLES AND PROCESSES
time.sleep(1)
income = float(input("Enter your monthly income in £: "))
time.sleep(1)
housingCost = float(input("Enter your monthly housing cost in £: "))
time.sleep(1)
electricBill = float(input("Enter your monthly electric bill in £: "))
time.sleep(1)
gasBill = float(input("Enter your monthly gas bill in £: "))
time.sleep(1)
waterBill = float(input("Enter your monthly water bill in £: "))
time.sleep(1)
councilTax = float(input("Enter your monthly council tax bill in £: "))
time.sleep(1)
essentialShop = float(input("Enter your monthly essential shopping costs in £: "))

expenditure = housingCost + electricBill + gasBill + waterBill + councilTax + essentialShop
disposableIncome = income - expenditure

#CONDITIONAL BLOCK - OUTPUTS
if disposableIncome >= 0:
    time.sleep(1)
    print(f"Your total expenditure is £{expenditure:.2f}.")
    time.sleep(1)
    print(f"Your disposable income is £{disposableIncome:.2f}.")
    time.sleep(1)
    print("You are not in debt or short of money for your expenditure.")
else:
    time.sleep(1)
    print(f"Your total expenditure is £{expenditure:.2f}.")
    time.sleep(1)
    print(f"Your disposable income is £{disposableIncome:.2f}.")
    time.sleep(1)
    print("You are in debt or short of money for your expenditure.")

