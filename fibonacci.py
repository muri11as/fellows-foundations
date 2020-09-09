n = int(input())
fibs = [1,1]
for i in range(0,n):
	if i > 1:
		fib = fibs[i-2] + fibs[i-1]
		fibs.append(fib)
		
	print (fibs[i])