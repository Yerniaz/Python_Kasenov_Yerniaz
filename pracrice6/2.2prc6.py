a = [-1, 2, -3, 4, -5, 6]
positive=[]
negative=[]
for i in range(len(a)):
    if a[i] < 0:
        negative.append(a[i])
    elif a[i] > 0:
        positive.append(a[i])
print('Negative array: ', negative)
print('Positive array: ', positive)
