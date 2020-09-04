amt = float(input())
quarters = 0
dimes = 0
nicks = 0
pens = 0
if (amt >= .25):
	quarters = int(amt//.25)
amt = amt - (quarters*.25)
amt = round(amt%1,2)
if (amt >= .10):
	
	dimes = int(amt // .10)
amt = amt - (dimes*.10)
amt = round(amt%1,2)
if(amt >= .05 and amt < .10):
	
	nicks = int(amt //.05)
amt = amt -(nicks*.05)
amt = round(amt%1,2)
if (amt>0.0 and amt <.05):
	pens = int(amt/.01)


print("The coins are",quarters,"quarters,",dimes,"dimes,",nicks,"nickels and",pens,"pennies")