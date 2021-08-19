import math

a = str(input())
b = float(input())
c = float(input())

if a == 'Monaco':
    print('The Grand Prix of Monaco runs over 78 laps (260.52 km).')
elif 120/c*b < 305:
    laps = math.ceil(120/c)
    km = b * laps
    print('The Grand Prix of ' + str(a) + ' runs over ', laps, ' laps ' + '(', km, ' km).', sep = '')
elif 120/c*b > 305:
    laps = math.ceil(305/b)
    km = (b * laps)
    print('The Grand Prix of ' + str(a) + ' runs over ', laps, ' laps ' + '(', km, ' km).', sep = '')