def evenOdd(a):
    even = 0
    odd = 0
    for i in str(a):
        if int(i) % 2 ==0:
            even += 1
        else:
            odd += 1
    return even, odd

def step(a):
    even = 0
    odd = 0
    for i in str(a):
        if int(i) % 2 ==0:
            even += 1
        else:
            odd += 1
    return int(str(even) + str(odd) + str(even + odd))

def steps(a):
    count = 0
    while a != 123:
        even = 0
        odd = 0
        for i in str(a):
            if int(i) % 2 == 0:
                even += 1
            else:
                odd += 1
        a = int(str(even) + str(odd) + str(even + odd))
        count += 1
    return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
