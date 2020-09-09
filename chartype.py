charmander = input()

if type(charmander) == str and charmander.islower():
	print (charmander, "is a lowercase letter.")
elif type(charmander) == str and charmander.isupper():
	print (charmander, "is an uppercase letter.")
elif type(charmander) == str and charmander.isdigit():
	print (charmander, "is a digit.")
else:
	print (charmander, "is a non-alphanumeric  character.")