import math
x = 1
y = 4
z = 3
ctg = math.cos(y) / math.sin(y)
first = math.fabs(ctg + 6)
cube_root = first ** (1./3.)
second = math.sqrt(math.pow(x+1,3)/ (4*y - 2*z))
print()
print(cube_root + second)
