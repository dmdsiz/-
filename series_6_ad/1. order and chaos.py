def group(cards, num):
    A=[]
    B=[]
    sum=0
    sum2=0
    cards = tuple(cards)
    if type(num) is int:       # to distinguish num, because it comes up with number or list
        B.append(num)
    else:
        for j in num:
            if type(j) is int:       # if num is minus or num is string then it will makes error
                if j <= 0:
                    assert '', 'invalid grouping'
                else:
                    sum2+=j
                    B.append(j)
            else:
                assert '', 'invalid grouping'
    for i in range(len(cards)):
        if len(B) >= 2 and sum2 ==len(cards):    # if num is number list will be divided into groups which number of elements are num
            for h in B:                          # if num is list then, cards should make its groups of elements like list
                A.append(cards[sum:h + sum])
                sum += h
            return A
        if len(B) >= 2 and sum2 != len(cards):
            assert '', 'invalid grouping'
        for j in B:
            if i % j == 0:
                A.append((cards[i:i+j]))
            if len(cards) % j != 0:
                assert '', 'invalid grouping'
    return A
def riffle_shuffle(pile1,pile2):
    A = []
    B = []
    if len(pile1) == len(pile2):                     # length of pile1 & pile2 should be same
        for i in range(len(pile1)):
            A.append(pile1[i])
            A.append(pile2[i])
        for j in A:
            for h in j:
                B.append(h)
        return B
    else:
        assert '', 'different number of groups'
def mixed_pairs(new_pile):          # new_pile is result of riffle_shuffle(pile1, pile2)
    A = []
    B=[]
    C=[]
    count = 0
    count2 = 0
    for i in new_pile:
        for i in new_pile:             # in a pair, there should be different color C and S are same color so replace C to S
            i = i[-1]                  # and D to H
            A.append(i)
            A2 = ''.join(A)
            A3 = A2.replace('C', 'S')
            A4 = A3.replace('D', 'H')
    for i in A4:
        C.append(i)
    for i in C:
        if 'S' in i:                # this counting is for length of result because it should be even.
            count +=1
        else:
            count2 += 1
    if len(C) %2 !=0:
        assert '', 'odd number of cards'
    if count == count2:
        for i in range(len(C)):
            if i %2 ==0 and i < len(C):
                if C[i] != C[i+1]:
                    B.append(1)
                else:
                    B.append(0)
    result = sum(B)
    if result is len(C)//2:
        return True                 # if number of red and black are same return True or not return False
    if result is not len(C)//2:
        return False
    if count != count2:         # if number of pairs doesn't match return False
        return False