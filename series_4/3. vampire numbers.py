import math
vampire_number = int(input())
count = 0
n = int(math.log10(vampire_number))
sorted_a=sorted(str(vampire_number))
for x in range(1,10**math.ceil(n/2)):
    for y in range(1,10**math.ceil(n/2)):
        if vampire_number == x*y:
            sorted_z = sorted(str(x)+str(y))
            sorted_x = sorted(str(x))
            sorted_y = sorted(str(y))
            if len(sorted_x) == len(sorted_y):
                if sorted_z == sorted_a:
                    if x < y :
                        count+=1
                        if vampire_number % 10**round(n/2) == 0:
                            print(vampire_number,'is not a vampire number.')
                        elif vampire_number % 10**round(n/2) != 0:
                            if count<2:
                                print(vampire_number,'is a vampire number.')
if count == 0:
    print(vampire_number,'is not a vampire number.')