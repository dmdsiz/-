def isISBN(code):
    '''
    >>> isISBN('9-9715-0210-0')
    True
    >>> isISBN('997-150-210-0')
    False
    >>> isISBN('9-9715-0210-8')
    False
    '''
    if not isinstance(code,str):
        return False
    groups = code.split('-')
    if tuple(len(e) for e in groups) != (1,4,4,1):
        return False
    code = ''.join(groups)
    if not code[:-1].isdigit():
        return False
    return checkdigit(code) == code[-1]
def checkdigit(code):
    check = sum((i+1)*int(code[i]) for i in range(9)) % 11
    return 'X' if check ==10 else str(check)

if __name__=='__main__':
    import doctest
    doctest.testmod()