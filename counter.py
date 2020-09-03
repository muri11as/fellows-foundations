print ("Please enter the number of coins:")
print ("#of quarters:")
quarters = input()
print ("#of dimes:")
dimes = input()
print ("#of nickels"
nickels = input()
print ("#ofpennies")
pennies = input()
quartertot = quarters * .25
dimestot = dimes * .10
nickeltot = nickels* .05
pennytot = pennies *.01
tot = quartertot + dimestot+nickeltot+pennytot
cents = tot % 1
dollars = tot // 1
print ("The total is ",dollars , "dollars and ", cents,"cents")