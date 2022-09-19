n = int(input())
a = [ int(input()) for i in range(n)]
max = a[0]
max_index = 0
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        max_index = i
print(max_index + 1)
