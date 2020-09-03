print("Enter dollar and cent amount:")
amt = float(input())
if amt >= .25:
	quarters = amt//.25
	amt = amt - (quarters*.25)
amt = round(amt%1,2)
elif amt >= .10:
	dimes = amt // .10
	amt = amt - (dimes*.10)
amt = round(amt%1,2)
elif(amt >= .05 and amt < .10):
	nicks = amt //.05
	amt = amt -(nickels*.05)
amt = round(amt%1,2)
else:
	pens = amt//.01


print("The coins are",quarters,"quarters,",dimes,"dimes,",nickels,"nickels and",pens,"pennies")