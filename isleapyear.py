
def isleapyear(num):
	if num % 4 == 0 and num % 100 == 0 and num % 400 == 0:
		return True
	elif num % 4 == 0 and num % 100 != 0:
		return True
	else:
		return False

#def main():
#	year = int(input())
#	isleapyear(year)
	

#main()
