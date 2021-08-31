import math
def iszapreadable(a):
    x = []
    d = 0
    for i in range(len(a)):
        x.append(i + 1)
    for j in range(len(x)):
        d += j
        f = d % len(x)
        x[f] = j + 1
    A = []
    B = []
    C= []
    for i in range(len(a)):
        if len(a) - (2 * i + 1) > 0:
            A.append(len(a) - (2 * i + 1))
    for i in range(len(a)):
        if len(a) - (2 * i) > 0:
            B.append(len(a) - (2 * i))
    C = A+B
    if a == x or a == C:
        return True
    else:
        return False
def zapbook(a):
    A=[]
    B=[]
    if math.log2(a).is_integer():
        x = []
        d = 0
        for i in range(a):
            x.append(i + 1)
        for j in range(len(x)):
            d += j
            f = d % len(x)
            x[f] = j + 1
        return x
    if a%2 != 0:
        return []
    else:
        for i in range(a):
            if a-(2*i+1) >0:
                A.append(a-(2*i+1))
        for i in range(a):
            if a-(2*i) > 0:
                B.append(a-(2*i))
        return A+B
