def flip(sequance, burnt=None):
    answer = []
    if burnt == True:      # reverse the sequance and multiply (-1)
        for i in sequance:
            answer.append(i * (-1))
        answer.reverse()
    else:                # reverse the sequance
        for i in sequance:
            answer.append(i)
        answer.reverse()
    return tuple(answer)


def flip_top(sequance, num, burnt=None): # if burnt times(-1) and cut and filp at num
    sequance = list(sequance)
    A = []
    if burnt == True:
        sequance2 = sequance[:num]
        sequance2.reverse()
        for i in sequance2:
            A.append(i * (-1))
        answer = A + sequance[num:]
        return tuple(answer)
    else:
        answer = sequance[:num]
        answer.reverse()
        answer = answer + sequance[num:]
        return tuple(answer)


def find_largest(sequance, num):    # sort the sequance and find the number at position(num) and find the number at sequance
    abs_list = sorted(map(abs, list(sequance)))
    abs_list2 = abs_list[num - 1]
    answer = tuple(map(abs, list(sequance))).index(abs_list2)
    return answer + 1


def sorting_step(sequance, num, burnt=None):   # sort the sequance and find the number at position(num) and find the number at sequance and change the sequance.
    if burnt == True:                          # if burnt times (-1)
        c = find_largest(sequance, num)
        d = flip_top(sequance, c, burnt=True)
        e = flip_top(d, num, burnt=True)
        if e[num - 1] < 0:
            e = list(e)
            e[num - 1] = e[num - 1] * (-1)
    else:
        c = find_largest(sequance, num)
        d = flip_top(sequance, c)
        e = flip_top(d, num)
    return tuple(e)
def sorting_steps(sequance, burnt=None):
    A = []
    B = []
    A.append(sequance)
    y=sorted(sequance)
    if burnt == None or burnt ==False:
        for i in range(len(sequance)):
            sequance = sorting_step(sequance, len(sequance) - i)
            if sequance != y:
                A.append(sequance)
        for i in A:
            if i not in B:
                B.append(i)
    else:
        for i in range(len(sequance)):
            sequance = sorting_step(sequance, len(sequance) - i,burnt=True)
            if sequance != y:
                A.append(sequance)
        for i in A:
            if i not in B:
                B.append(i)
    return B
