day = input()
dlist = ["Mon","Tue", "Wed","Thr", "Fri", "Sat", "Sun"]
weekday  = 0
weekend = 0
if day in dlist[:5]:
	weekday = 1
else:
	weekend = 1
rate = 0
timeStart = int(input())
if ((weekday == 1 )and (timeStart < 800 or timeStart > 1800)):
	rate = .25
elif ((weekday == 1 )and ( 800 <= timeStart <= 1800)):
	rate = .40
else:
	rate =.15
	
dur = int(input())

cost = dur * rate

print("This call will cost $%.2f" % cost)

