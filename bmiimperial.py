pounds = float(input())
height = float(input())

lbkg = .453592
hmeter = .0254

#lbs = pounds * lbkg
#meters = height * hmeter
status="N/A"S

#bmi = lbs/(meters**2)
bmi = pounds/(height**2)
if bmi < 18.5:
	status = "Underweight"
elif 18.5 <= bmi < 25:
	status =  "Normal"
elif 25 <= bmi < 30:
	status = "Overweight"
else:
	status = "Obese"

print ("BMI is:",bmi, "Status is",status)