def profit(price,sequence):
    A=[]
    B=[]
    C=[]
    D=[]
    sum = 0
    count = 0
    if type(sequence) is str:
        for i in sequence:
            A.append(i)
            count +=1
            if i is 'B' or i is 'S' or i is '-':
                if len(price) == len(sequence): # price and squence are same so length should be same
                    if i is 'B':
                        B.append(count)
                        D.append(i)
                    if i is 'S':
                        C.append(count)
                        D.append(i)
                    if 'S' in sequence and 'B' in sequence:   # if bitcoins are bought then, it must be sold
                        if sequence.index('B') > sequence.index('S'):
                            assert '', 'invalid actions'
            else:
                assert '', 'invalid actions'
    else:
        assert '', 'invalid actions'
    if 'SS' in ''.join(D) or 'BB' in ''.join(D):  # as it was mentioned, bitcoins are must be sold after buying so sell,sell and buy,buy is not available
        assert '', 'invalid actions'
    if len(price) == len(sequence):
        if len(B) == len(C):
            for i in B:
                sum -= price[i-1]
            for i in C:
                sum += price[i-1]
            return sum
        else:
            assert '', 'invalid actions'
    else:
        assert '', 'invalid actions'
def maximal_profit(price):
    A = optimal_actions(price)
    sum = 0                      # by using optimal_actions(def) buy and sell can be visualize with sequance
    b=[]
    c=[]
    for i in range(len(A)):
        if A[i] is 'B':          # find the numbers when bitcoins are bought and sold because price and sequance are identical
            b.append(i)
        if A[i] is 'S':
            c.append(i)
    for i in b:
        sum -= (price[i])       # sum every price
    for i in c:
        sum += (price[i])
    return sum
def optimal_actions(price):
    sequence = []
    count = 0
    for i in range(len(price)):
        if i < len(price)-1 and price[i+1] - price[i] > 0 or i == len(price)-1 and price[i] - price[i - 1] < 0:
            sequence.append('B')
        if i < len(price)-1 and price[i+1] - price[i] < 0 or i == len(price)-1 and price[i] - price[i - 1] > 0:
            sequence.append('S')
        if i < len(price) - 1 and price[i + 1] - price[i] == 0 or i == len(price)-1 and price[i] - price[i - 1] == 0:
            sequence.append('-')
    if sequence[-1] == sequence[-2] or sequence[-1] == 'B':
        sequence[-1] = '-'
    if sequence[0] == 'S':        # after buying the bitcoin it must be sold when it's price is maximum and it must be bought when it's price is minimum
        sequence[0] = '-'
    for i in range(len(sequence)):
        if sequence[i] is 'B':
            count += 1
        if sequence[i] is 'S':
            count -= 1
        if count <0:
            sequence[i] = '-'
            count +=1
        if count > 1:
            sequence[i] = '-'
            count -=1
    if count != 0:
        sequence[-1] ='S'
    return ''.join(sequence)