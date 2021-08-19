a = float(input())
b = float(input())

if b >= 10000:
    print('supergiants (a)')
elif 1000 < b < 10000:
    print('supergiants (b)')
elif 100 < b < 1000 and a < 7500:
    print('bright giants')
elif 10 < b < 100 and a < 6000:
    print('giants')
elif 0.0001 < b < 0.01 and 5000 < a < 30000:
    print('white dwarfs')
elif b < 0.0001 and 3000 < a < 30000:
    print('white dwarfs')
else:
    print('main sequence')