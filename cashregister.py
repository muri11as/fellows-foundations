item1 = input()
item2 = input()
base = float(item1) + float(item2)
if item1 > item2:
	item2 = float(item2) * .5
else:
	item1 = float(item1) * .5

cardIn = input ()
if cardIn == 'Y' or cardIn == 'y':
	card = 1
else:
	card = 0
tax = input()

print("Base price = %.2f"% origbase)
base = float(item1) + float(item2)
if card == 1:
	disc = base * .1
else:
	disc = base
disc = base - disc
print("Price after discounts = %.2f"% disc)
tax = float(tax)/100
tot = disc + (disc * tax)

print("Total price = %.2f" %tot)



