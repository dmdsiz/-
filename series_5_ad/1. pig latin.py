def pigword(word):
    A = []
    if word == '-': # "-" this punctuation will be used for when "-" is alone
        return word
    if '...' in word: # when "..." run in for loop, it makes error because this def only can recognize one punctuation, so change it into "&"
        word.replace('...','&')
    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u' or word[0] == 'A' or word[0] == 'E' or word[
        0] == 'I' or word[0] == 'O' or word[0] == 'U' or word[0] == "'":
        return word + 'way'
    if 'qu' in word:
        for i in (word):
            if i is 'a' or i is 'e' or i is 'i' or i is 'o' or i is 'A' or i is 'E' or i is 'I' or i is 'O':
                A.append(i)
                return word[word.index(A[0])] + word[word.index(A[0]) + 1:] + word[:word.index(A[0])] + 'ay'

    else:
        for i in (word):
            if i is 'a' or i is 'e' or i is 'i' or i is 'o' or i is 'u' or i is 'A' or i is 'E' or i is 'I' or i is 'O' or i is 'U':
                A.append(i)
                if word[0].isupper() and A[0].islower():
                    return word[word.index(A[0])].upper() + word[word.index(A[0]) + 1:] + word[0].lower() + word[1:word.index(A[0])] + 'ay'
                elif word[0].isupper() and A[0].isupper:
                    return word[word.index(A[0])].upper() + word[word.index(A[0]) + 1:] + word[:word.index(A[0])] + 'ay'
                elif word[0].islower() and A[0].islower():
                    return word[word.index(A[0])] + word[word.index(A[0]) + 1:] + word[:word.index(A[0])] + 'ay'
                else:
                    return word[word.index(A[0])].upper() + word[word.index(A[0]) + 1:] + word[:word.index(A[0])] + 'ay'
        else:
            for i in (word):
                if i is 'a' or i is 'e' or i is 'i' or i is 'o' or i is 'u' or i is 'A' or i is 'E' or i is 'I' or i is 'O' or i is 'U':
                    A.append(i)
            return word[word.index(A[0])].lower() + word[word.index(A[0]) + 1:] + word[:word.index(A[0])] + 'ay'


def piglatin(sentence):
    A=[]
    B=[]
    C=[]
    sentence2=sentence
    if '...'in sentence:
        sentence=sentence.replace('...','&')
    if '(' in sentence:
        sentence=sentence.replace('(','')    #removing "()"
    if ')' in sentence:
        sentence=sentence.replace(')','')
    punctuation = '''!()[]-{};:'"\,<>./?@#$%^&*_~'''
    for i in sentence.split( ):
        A.append(i)               # list "A" is for normal word and list "B" is for changed word
        B.append(pigword(i))
    for j in A:
        for u in punctuation:
            if u in j:
                if j == '-' and len(j) == 1:
                    c= '-'
                    b=j
                    A[A.index(c)] = b
                    B[A.index(b)] = b
                else:
                    t, h = j.split(u)
                    o = t + h
                    b=(pigword(o)+u)
                    c = o+u
                    if j[-1] is u:
                        A[A.index(c)] = b
                        B[A.index(b)] = b
                    if j[-1] is not u:
                        C.append(len(j))
                        if j[0] == u:
                            qwe = u + j[j.index(u) + 1:] + 'way'
                            A[A.index(j)] = qwe
                            B[A.index(qwe)] = qwe
                            break
                        if (j[j.index(u) + 1:]) == 'll':
                            qwe = pigword(j[:j.index(u)]) + u + 'llay'
                            A[A.index(j)] = qwe
                            B[A.index(qwe)] = qwe
                        if len(j[j.index(u)+1:]) == 1:
                            qwe= pigword(j[:j.index(u)]) + u + j[j.index(u)+1:] + 'ay'
                            A[A.index(j)] = qwe
                            B[A.index(qwe)] = qwe
                        else:
                            if (j[j.index(u) + 1:]) != 'll':
                                qwe = pigword(j[:j.index(u)]) + u + pigword(j[j.index(u)+1:])
                                A[A.index(j)] = qwe
                                B[A.index(qwe)] = qwe
    sds=' '.join(B)
    if '&' in ' '.join(B):
        return ' '.join(B).replace('&','...') # change "&" into original punctuation "..."
    if '(' in sentence2:     # brackets are removed above,but it need brackects, so they were added after the loop
        return '('+sds+')'
    return ' '.join(B)