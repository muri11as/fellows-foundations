print ("Please enter the number of coins:")

int quarters = input("#of quarters:")
quartertot = quarters * .25
int dimes = input("#of dimes:")
dimestot = dimes * .10
int nickels = input("#of nickels:")
nickeltot = nickels * .05
int pennies = input("#ofpennies:")
pennytot = pennies *.01

tot = quartertot + dimestot + nickeltot + pennytot
cents = tot % 1
dollars = tot // 1
print ("The total is ",dollars , "dollars and ", cents,"cents")