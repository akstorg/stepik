a = int(input())
b = int(input())
op = str(input())

if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '/':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a/b)


