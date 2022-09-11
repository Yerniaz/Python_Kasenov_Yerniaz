import math

AB = input ("First leg length:")
AC = input ("Length of the second leg:")

AB = float (AB)
AC = float (AC)

BC = math.sqrt (AB ** 2 + AC ** 2)

S = (AB * AC) / 2

print ("Triangle area: " , S)

