import math
def preprocess(p, x, y, n):
	for i in range(n):
		p[i] = x[i] * x[i] + y[i] * y[i]
	p.sort()
def query(p, n, rad):

	start = 0
	end = n - 1
	while ((end - start) > 1):
		mid = (start + end) // 2
		tp = math.sqrt(p[mid])

		if (tp > (rad * 1.0)):
			end = mid - 1
		else:
			start = mid

	tp1 = math.sqrt(p[start])
	tp2 = math.sqrt(p[end])

	if (tp1 > (rad * 1.0)):
		return 0
	elif (tp2 <= (rad * 1.0)):
		return end + 1
	else:
		return start + 1

if __name__ == "__main__":
	x = [ 1, 2, 3, -1, 4 ]
	y = [ 1, 2, 3, -1, 4 ]
	n = len(x)
	p = [0] * n
	preprocess(p, x, y, n)
	print(query(p, n, 3))
	print(query(p, n, 32))
