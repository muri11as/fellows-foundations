print ("Please enter the number of coins:")
quarters = int(input())
dimes = int(input())
dimestot = dimes * .1

nickels = int(input())
nickeltot = nickels * .05

pennies = int(input())
pennytot = pennies *.01


tot = (quarters*.25) + (dimes*.1) + (nickels*.05) + (pennies*.01)

rnded = round(tot,2)

strtot = str(rnded)
dollars = int(tot//1)
cent = int((strtot.split('.')[1]))

print ("The total is",dollars , "dollars and", cent,"cents")