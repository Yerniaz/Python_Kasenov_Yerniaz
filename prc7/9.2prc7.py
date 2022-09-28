def prdArr(n):
    prd = 1
    for i in n:
        prd *= i
    return prd

for i in range(3):
    a = random.sample(range(100), 15)
    print(a)
    print(prdArr(a))
    print(meanArr(a,sumArr(a)))
