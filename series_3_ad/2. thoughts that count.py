red_white = int(input())        # number of red and white roses
white_blue = int(input())       # number of white and blue roses
operator = str(input())         # > or <
# at least two roses for every color

List=[]
for i in range (2, white_blue):         # i is blue, number of blue roses is less than number of white and blue roses
    white = white_blue - i
    red = red_white - white
    List.append(i)         # insert i into List (empty list)
    if operator == '<':
        if int(List[i-2]) + red < white_blue:        # number of blue and red roses < number of white and blue roses
            if red >= 2:
                if white >= 2:
                    print(i,white,red, sep='\n')        # showing out in three separate lines, by using sep='\n'
    if operator == '>':
        if int(List[i - 2]) + red > white_blue:         # number of blue and red roses> number of white and blue roses
            if red >= 2:
                if white >= 2:
                    print(i, white, red, sep='\n')      # showing out in three separate lines, by using sep='\n'