import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

a = 6371 * math.acos(math.sin(x1*math.pi/180)*math.sin(x2*math.pi/180)+math.cos(x1*math.pi/180)*math.cos(x2*math.pi/180)*math.cos(y1*math.pi/180-y2*math.pi/180))

print('The great-circle distance is',round(a),'km.')