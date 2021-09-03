def isISBN10(code):
    if not (isinstance(code, str) and len(code) == 10 and code[:9].isdigit()):
        return False
    checkdigit = sum((i + 1) * int(code[i]) for i in range(9)) % 11
    x10 = code[9]
    return (checkdigit == 10 and x10 == 'X') or x10 == str(checkdigit)

def isISBN13(code):
    if not(isinstance(code, str) and len(code) == 13 and code.isdigit()):
        return False
    checkdigit = sum((3 if i % 2 else 1) * int(code[i]) for i in range(12))
    checkdigit = (10 - checkdigit % 10) % 10
    return checkdigit == int(code[-1])

def isISBN(code, isbn13 = True):
    return isISBN13(code) if isbn13 else isISBN10(code)

def areISBN(codes, isbn13 = None):
    eval = []
    for code in codes:
        if isinstance(code, str):
            if isbn13 is None:
                if len(code) == 13:
                    eval.append(isISBN(code, True))
                else:
                    eval.append(isISBN(code, False))
            else:
                eval.append(isISBN(code, isbn13))
        else:
            eval.append(False)
    return eval