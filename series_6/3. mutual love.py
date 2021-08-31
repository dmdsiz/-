def positions(a):
    A=[]
    for i in a:
        A.append(ord(i.lower())-97)
    return tuple(A)
def ismutual(a,b):
    a=list(a)
    a.sort()
    A = []
    B = []
    C = []
    D = []
    for i in range(len(a)):
        if i < len(a) // 2:
            A.append(a[i])
        if len(a) // 2 <= i <= len(a):
            B.append(a[i])
    for i in range(len(A)):
        if i < len(A) - 1:
            C.append(abs(A[i + 1] - A[i]))
    for i in range(len(B)):
        if i < len(B) - 1:
            D.append(abs(B[i + 1] - B[i]))
    if sorted(C) == sorted(D):
        return True
    else:
        return False
def mutual_love(x):
    a = positions(x)
    a = list(a)
    a.sort()
    for i in range(len(a)):
        if a[1] - a[0] == a[len(a) - 1] - a[len(a) - 2] and a[2] - a[1] == a[len(a) - 2] - a[len(a) - 3]:
            return True
        else:
            return False