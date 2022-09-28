print('There is only 3 geom. fig. "Rectangle", "Triangle", "Parallelogram"')
def calculate(geom_fig):
    if geom_fig == 'Rectangle':
        a = int(input("Length: "))
        b = int(input("Breath: "))
        rect = a * b
        print('Rectangle area is = ', rect)
    elif geom_fig == 'Triangle':
        c = int(input('Height: '))
        d = int(input('Breath: '))
        trian = 0.5 * c * d
        print('Triangle area is = ', trian)
    elif geom_fig == 'Parallelogram':
        f = int(input('Base: '))
        g = int(input('Height: '))
        para = f * g
        print('Parallelogram area is = ', para)
    else:
        print('Sorry! Yerniazs program dont know any geom fig)))')
geom_fig = input('Input geom. fig: ')
calculate(geom_fig)
