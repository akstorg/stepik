a = int(input())
b = int(input())
c = int(input())

big = a
aver = b
small = c

if a >= b and a >= c:
    big = a
elif b >= a and b >=c:
    big = b
else:
    big = c


# if b >= a:
#     big = b
#     if c >= b:
#         big = c

if a <= b and a <=c:
    small = a
elif b <= a and b <=c:
    small = b
else:
    small = c

aver = (a + b +c) - big - small

print(big)
print(small)
print(aver)









