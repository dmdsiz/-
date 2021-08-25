def longestPolydivisiblePrefix(a):
    count = 0
    for i in range(len(str(a))):
        if int(str(a)[:i+1]) % (i+1) != 0:
            count +=1
            return int(str(a)[:i])
    if count == 0:
        return int(str(a)[:len(str(a))+1])

def isPolydivisible(a):
    answer = longestPolydivisiblePrefix(a)
    if answer == a:
        return True
    else:
        return False

def polydivisibleExtensions(a):
    count = 0
    answer = longestPolydivisiblePrefix(a)
    if answer == a:
        for i in range(10):
            if (a*10+i) % (len(str(a*10+i))) ==0:
                count += 1
    return(count)