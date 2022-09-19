n = int(input('Введиту длину массива: '))
a=[]
b = 11145789
for i in range(n):
        print('Введите', i, ' элемент: ')
        a.append(int(input()))
for i in range(n):
    if a[i] < b:
        b = a[i]
print(b)
    
