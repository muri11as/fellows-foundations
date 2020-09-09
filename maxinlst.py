def max_val(lst):
	maxy = lst[0]
	for i in range(0,len(lst)-1):
		if lst[i] >= maxy:
			maxy = lst[i]
	return maxy