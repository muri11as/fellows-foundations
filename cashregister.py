item1 = input()
item2 = input()
cardIn = input ()
if cardIn == 'Y' or cardIn == 'y':
	card = 1
else:
	card = 0
tax = input()

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



