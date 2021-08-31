def average(x):
    a = 0
    for i in x:
        a += i
    return a/len(x)
def move1(seq1, seq2, seq3):
    for i in range(len(seq3)):
        seq1.remove(seq3[i])
    for j in range(len(seq3)):
        seq2.append(seq3[j])
def move2(seq1, seq2, seq3):
    seq1 = list(seq1)
    seq2 = list(seq2)
    for i in range(len(seq3)):
        seq1.remove(seq3[i])
    for j in range(len(seq3)):
        seq2.append(seq3[j])
    return (seq1, seq2)
def iswillrogers(a,b,c):
    aa = average(a)
    bb = average(b)
    move2(a,b,c)
    A,B=move2(a,b,c)
    AA = average(A)
    BB = average(B)
    if AA > aa and BB>bb:
        return True
    else:
        return False