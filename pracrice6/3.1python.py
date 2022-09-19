def EvenOddSum(a, n):
	even = 0
	odd = 0
	for i in range(n):
		if i % 2 == 0:
			even += a[i]
		else:
			odd += a[i]
	
	print ("Even index positions sum ", even)
	print ("nOdd index positions sum ", odd)
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)

EvenOddSum(arr, n)
