from datetime import date
name = str(input())
b = int(input())
count = 0
for x in range(1,1000):
    if b == x ** 2 - x:
        count += 1
        if b + x >= date.today().year:
            print(name + ' turns ', x, ' in ', x + b, '.', sep='')
        elif b + x < date.today().year:
            print(name + ' was ', x, ' in ', x + b, '.', sep='')

if count == 0:
    print(name + ' is not a member of the Confederacy of Squares.')