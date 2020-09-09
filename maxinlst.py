def max_val(lst):
	maxy = lst[0]
	for i in lst:
		if lst[i] >= maxy:
			maxy = lst[i]
	return maxy