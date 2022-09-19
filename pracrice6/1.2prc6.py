n = int(input('Введиту длину массива: '))
a=[]
sum = 0
for i in range(n):
        print('Введите', i, ' элемент: ')
        a.append(int(input()))
for i in range(n):
        sum += a[i]
for i in range(n):
    if a[i] == 0:
        a [i] = sum / n
print(a[i])

