def max_abs_val(lst):
	maxy = 0
	for i in range(0,len(lst)):
		abby = abs(lst[i])
		if abby >= maxy:
			maxy = abby
	return maxy
			