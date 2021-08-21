a = int(input())

while True:
    x = input()
    if x == 'stop':
        print('You end up with', a, 'dollar.')
        break
    y = str(input())
    z = str(input())
    if x == 'all':
        b = a
        if y == z:
            a = a + b
        else:
            print('You end up with', 0, 'dollar.')
            break
    if x != 'all':
        x = int(x)
        if x < a:
            if y == z:
                a = a + int(x)
            elif y != z:
                a = a - int(x)
        elif x > a:
            print('You cannot bet', x, 'dollar if you only have', a, 'dollar.')
            break