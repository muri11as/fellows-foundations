print ("Please enter the number of coins:")
quarters = int(input("#of quarters:"))
quartertot = quarters * .25
dimes = int(input("#of dimes:"))
dimestot = dimes * .10
nickels = int(input("#of nickels:"))
nickeltot = nickels * .05
pennies = int(input("#ofpennies:"))
pennytot = pennies *.01

tot = float(quartertot + dimestot + nickeltot + pennytot)
cents = tot % 1
dollars = tot // 1
print ("The total is ",dollars , "dollars and ", cents,"cents")