import re
def numeronym(a):
    if len(a) <= 3:
        x = str(a)
    else:
        x = str(str(a[0]) + str(len(a) - 2) + str(a[(len(a) - 1)]))
    return x

def template(a):
    aa=[]
    count = 0
    y = re.findall('\d+',a)
    y2 = ''.join(y)
    if y2 in a:
        count +=1
        return (a.replace(y2, '.' * int(y2)))
    if count == 0:
        for i in range(len(y2)):
            if y[i] in a:
                aa.append(y[i])
        return (a.replace(aa[0], '.' * int(aa[0])).replace(aa[1], '.' * int(aa[1])))

def isnumeronym(a,b):
    answer=template(a)
    B = b.lower()
    A = answer.lower()
    if len(answer) == len(b):
        if A[:A.index('.')] == B[:A.index('.')]:
            return True
        else:
            return False
    else:
        return False