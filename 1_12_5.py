a = int(input())
b = int(input())
c = int(input())



big = a
small = c
aver = b

if b >= a:
    big = b
    if c >= b:
        big = c

if big == c and a >= b:
    small = b
    aver = a
elif big ==c and a <= b:
    small = a
    aver = b
else:
    print('other')
print(big)
print(small)
print(aver)









