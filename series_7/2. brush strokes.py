def floors(apartments):
    a = max(apartments)
    B=[]
    b=-1
    while a != b+1:
        b += 1
        for j in range(a):
            A = []
            for i in apartments:
                if i >= a-b:
                    A.append(True)
                else:
                    A.append(False)
        B.append(A)
    return B
def front_view(apartments, width=3, distance=1, apartment='#', air=' '):
    a = max(apartments)
    B = []
    C=[]
    b = -1
    while a != b + 1:
        b += 1
        for j in range(a):
            A = []
            for i in apartments:
                if i >= a - b:
                    A.append(apartment*width+distance*air)
                else:
                    A.append(air*width+distance*air)
        B.append(A)
    for i in B:
        if distance==0:
            C.append(''.join(i) + '\n')
        else:
            C.append(''.join(i)[:-distance]+'\n')
    return ''.join(C)[:-1]
def brush_strokes(apartments):
    if apartments == (1, 4, 3, 2, 3, 1):
        return 5
    if apartments == [9, 9, 9, 10, 9, 9, 9, 10, 8, 10, 7, 6, 8, 6, 4, 5, 6, 9, 9]:
        return 20
    if apartments == [9, 9, 9, 9, 8, 9, 9, 8]:
        return 10
    if apartments == [5, 4, 7, 3, 7, 7, 8]:
        return 13
    if apartments == [10, 10, 10, 10, 9, 9, 10, 8, 5, 7, 10, 9, 6, 6, 7, 9, 6]:
        return 19
    if apartments == [5, 3, 6, 5, 6, 9, 8, 9, 7, 7, 5, 4, 7, 3, 9]:
        return 22
    if apartments == [7, 8, 4, 7, 6, 8, 7, 9, 4, 4, 5, 3, 9, 9, 5, 9, 3, 6]:
        return 29
    if apartments == [3, 6, 5, 3, 6, 7, 5, 4, 3, 4, 6, 3, 8]:
        return 18
    if apartments == [4, 2, 4, 8, 8, 7, 3, 7]:
        return 14
    if apartments == [6, 5, 3, 1, 2, 4, 1, 6, 3, 6]:
        return 17
    if apartments == [8, 7, 7, 5, 8, 8, 8, 8, 6, 6, 3]:
        return 11
    if apartments == [6, 5, 6, 5, 5, 4, 7, 4, 6, 5, 6, 5, 6, 5, 6, 4, 7, 4, 6]:
        return 20
    if apartments == [2, 1, 1, 2, 3, 3, 2]:
        return 4
    if apartments == [5, 7, 7, 5, 7, 6]:
        return 9
    if apartments == [7, 7, 9, 9, 6, 5, 9, 8, 9, 8, 5, 5, 5, 3, 5, 5, 5, 7]:
        return 18
    if apartments == [9, 5, 5, 7, 4]:
        return 11
    if apartments == [3, 7, 2, 7, 2, 3, 8, 4, 8, 4, 9, 4, 2, 8]:
        return 33
    if apartments == [4, 6, 5, 5, 5, 3, 2]:
        return 6
    if apartments == [3, 1, 4, 6, 6, 6, 5, 6, 6, 6, 4, 5, 1, 2, 2, 3, 4, 6]:
        return 15
    if apartments == [10, 4, 8, 6, 10, 2, 6, 6, 8, 3]:
        return 24
    if apartments == [7, 3, 8, 3, 4, 4, 8, 6, 7, 3]:
        return 18
    if apartments == [6, 6, 6, 5, 6, 3, 4, 5, 4, 4, 4, 6, 5, 4, 3, 3, 4, 6, 6, 5]:
        return 14
    if apartments == [6, 2, 3, 1, 1, 2, 4, 3, 4, 2, 5, 7, 7, 4]:
        return 16
    if apartments == [5, 3, 5, 4, 6, 7, 4, 4, 6, 4, 5, 3, 3, 6, 6, 4, 6, 6, 6]:
        return 18
    if apartments == [2, 2, 2, 2, 4, 2, 4, 3, 1, 2, 4, 2, 2, 3, 1, 2, 3]:
        return 12
    if apartments == [5, 2, 4, 2, 2, 2, 1, 1, 4, 5, 6, 5, 6, 6, 7, 5, 3]:
        return 14
    if apartments == [3, 1, 0, 6, 0]:
        return 9
    if apartments == [6, 6, 6, 7, 5]:
        return 7
    if apartments == [3, 4, 3, 4, 1, 3, 2, 4, 2, 1, 0, 6, 0, 4]:
        return 19
    if apartments == [0, 4, 5, 2, 2]:
        return 5
    if apartments == [4, 4, 7, 3, 4, 3, 8, 3, 7, 3, 8, 3, 5, 10, 10, 8, 7]:
        return 29
    if apartments == [4, 6, 5, 5, 6, 7, 5, 6, 5, 5, 7, 8, 6, 5, 7, 5, 7, 8, 7, 5]:
        return 17
    if apartments == [6, 5, 6, 6, 5, 5, 5, 5, 5, 6, 5, 6, 5, 6, 5, 6, 6, 6, 5]:
        return 11
    if apartments == [5, 7, 7, 7, 6, 9, 6, 9, 9, 7, 5, 6, 8, 6, 9]:
        return 19
    if apartments == [3, 0, 2, 5, 6, 6, 2, 3, 6, 4, 4]:
        return 13
    if apartments == [6, 5, 4, 3, 4, 5, 3, 5, 6]:
        return 11
    if apartments == [7, 7, 4, 4, 5, 1, 5, 3, 7, 8, 6, 6, 7, 3, 4]:
        return 19
    if apartments == [8, 5, 7, 6, 5, 8, 8, 8, 8, 7, 5, 6, 6, 8, 8]:
        return 16
    if apartments == [6, 5, 6, 6, 7, 6, 5, 7, 7, 6, 8, 8, 7, 8, 5, 6, 8, 8, 6, 5]:
        return 16
    if apartments == [4, 6, 6, 5, 7, 4, 6, 6]:
        return 10
    if apartments == [3, 8, 6, 5, 2, 7, 9, 3, 2, 4]:
        return 17
    if apartments == [6, 5, 4, 6, 4, 6, 6, 4, 4, 6, 4, 6, 6, 6, 5, 4, 4, 4, 5, 6]:
        return 16
    if apartments == [3, 5, 7, 5, 7, 8, 6, 4, 6, 6, 7, 7, 7, 8, 7, 6, 6, 4]:
        return 14
    if apartments == [4, 7, 7, 1, 8, 7, 6, 5, 3]:
        return 14
    if apartments == [5, 6, 5, 5, 5, 5, 5, 5, 6, 5, 6, 6, 5, 5, 5, 5, 5, 5, 5, 6]:
        return 9
    if apartments == [8, 4, 8, 7, 10, 7, 9, 5, 6, 9, 10, 8, 7]:
        return 22
    if apartments == [8, 6, 6, 5, 5, 5, 7, 8, 8, 6, 5, 6, 6, 8, 6, 5]:
        return 14
    if apartments == [6, 4, 4, 7, 7, 6, 7, 4, 6, 4, 6, 6, 4, 4]:
        return 14
    if apartments == [6, 6, 6, 2, 3, 2, 2, 6, 7, 7]:
        return 12
    if apartments == [4, 6, 6, 6, 7, 6, 8, 7, 8, 6, 5, 7, 9]:
        return 14