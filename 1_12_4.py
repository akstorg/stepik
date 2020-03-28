print('введите фигуру')
fig = str(input())
# a = int(input())

if fig == 'круг':
    print('enter radius')
    r = int(input())
    p = 3.14 * r**2
    print(p)



if fig == 'треугольник':
    print('enter a')
    a = int(input())
    print('enter b')
    b= int(input())
    print('enter c')
    c = int(input())
    p = sum([a, b, c]) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)