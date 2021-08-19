a = int(input())
b = int(input())
c = int(input())
d = str(input())
e = str(input())

if b <= a <= c:
    print('just right')
elif b > a:
    print('too '+d)
else:
    print('too '+e)