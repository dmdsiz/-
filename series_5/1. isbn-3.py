def isISBN(code):
    """
    checks wheter or not the code is valid
    Return True is the argument is a string that contains a valid ISBN-10 code,
    False otherwise.
    >>> isISBN('9971502100')
    True
    >>> isISBN('9971502108')
    False
    >>> isISBN('53WKEFF2C')
    False
    >>> isISBN(4378580136)
    False
    """
    # check if the given code is a string
    # note : isinstance is a Python built-in function that returns a Boolean
    # value that indicates whether or not the first argument is an object
    # that has a data type equal to the second argument passed to the function
    if not isinstance(code, str):
        return False
    # check if the given code contains 10 characters
    if len(code) != 10:
        return False
    # check if the first nine characters of the given code are digits
    if not code[:9].isdigit():
        return False
    checkdigit = int(code[0])
    for i in range(2, 10):
        x = int(code[i - 1])
        checkdigit += i * x
    checkdigit %= 11

    x10 = code[9]
    # print check digit
    return(checkdigit == 10 and x10 == 'X') or x10 == str(checkdigit)

if __name__ == '__main__':
    import doctest
    doctest.testmod()