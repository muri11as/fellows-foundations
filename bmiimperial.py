pounds = float(input())
height = float(input())

lbkg = .453592
hmeter = .0254

lbs = pounds * lbkg
meters = height * hmeter

bmi = lbs/(meters**2)

print ("BMI is:",bmi)