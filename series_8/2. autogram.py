def letter_frequencies(sentence):
    w = {}
    for x in sentence:
        if x.isalpha() == True:
            if x.lower() not in w:
                w[x.lower()] = 1
            else:
                w[x.lower()] += 1
                
    return w

def letter_positions(sentence):
    w = {}
    point = 0
    while True:
        if sentence[point].isalpha() == True:
            if sentence[point].lower() not in w:
                w[sentence[point].lower()] = {point}
            else:
                w[sentence[point].lower()].update({point})
        point += 1
        if point == len(sentence):
            break
    return w