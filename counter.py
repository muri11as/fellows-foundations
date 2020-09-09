#print ("Please enter the number of coins:")
quarters = int(input())
dimes = int(input())
dimestot = dimes * .1

nickels = int(input())
nickeltot = nickels * .05

pennies = int(input())
pennytot = pennies *.01


tot = (quarters*.25) + (dimes*.1) + (nickels*.05) + (pennies*.01)

dollars = int(tot//1)
tot = round(float(tot),2)
cent = str(tot).rsplit('.')[1]

print ("The total is",dollars,"dollars and", cent,"cents")