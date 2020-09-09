def max_abs_val(lst):
	maxy = 0
	for i in lst:
		abby = abs(lst[i])
		if abby >= maxy:
			maxy = abby
	return maxy
			