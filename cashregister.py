item1 = input("Enter price of first item:")
item2 = input("Enter price of second item:")
cardIn = input ("Does customer have a club card? (Y/N):")
if cardIn == 'Y' or cardIn == 'y':
	card = 1
else:
	card = 0
tax = input("Enter tax rate. e.g. 5.5 for 5.5% tax: ")

base = float(item1) + float(item2)

#base = (base,2)
print("Base price = %.2f"% base)
if card == 1:
	disc = base * .1
else:
	disc = base
disc = base - disc
print("Price after discounts = %.2f"% disc)
tax = float(tax)/100
tot = disc - (disc * tax)

print("Total price = %.2f" %tot)



