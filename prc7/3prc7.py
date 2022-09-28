import math
first = []
second = []

for i in range(2):
    print('Выведите катет ', i , ' элемент первого треугольника: ')
    first.append(int(input()))
for i in range(2):
    print('Выведите катет ', i , ' элемент второго треугольника: ')
    second.append(int(input()))
    
st = math.sqrt(pow(first[0],2)+pow(first[1],2))
nd = math.sqrt(pow(second[0],2)+pow(second[1],2))
if st < nd:
    print('Вторая гипотенуза больше ', nd)
elif st > nd:
    print('Первая гипотенуза больше ', st)
else:
    print('Они равны')
