left_side = str(input())
right_side = str(input())
Sum = left_side[::-1]+right_side  # left_side is reversed so [::-1] is used.

print(Sum) # first line of output
while Sum != right_side+left_side[::-1]: # run the while loop until Sum is right_side+left_side[::-1] (<- last line)
    for i in left_side[::-1]:
        if Sum.index(i) < len(Sum)-1: # find the index where is 'i', why len(Sum)-1? because max index of Sum is len(Sum)-1
            if Sum[Sum.index(i)+1] in right_side:
                Sum = Sum[:Sum.index(i)] + Sum[Sum.index(i)+1] + Sum[Sum.index(i)] + Sum[Sum.index(i)+2:]
    print(Sum)                       # if the letter of the left side and the right side face each other then
                                     #  switch them and make a new Sum by using index and print it