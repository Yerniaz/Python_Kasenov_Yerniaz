import math
x = 3
y = 0.2
first = 5*x*y/(math.pow(x,3)-4)
second = math.exp(math.pow(x,2))
cos = math.cos(y) ** 2
third = math.sqrt(cos - y*y)
print()
print(first + second + third)
